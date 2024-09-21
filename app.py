from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras
import json
import re
load_dotenv()

app = Flask(__name__)


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    city = request.args.get('city')
    food_type = request.args.get('food_type')
    price_level = request.args.get('price_level')
    positions = fetch_competitor_restaurants(city, food_type, price_level)
    return jsonify(positions)


@app.route('/rent', methods=['GET'])
def get_rents():
    try:
        cityId = request.args.get('cityId')
        api_key = os.getenv('LOOP_API')
        listing_endpoint = 'https://loopnet-api.p.rapidapi.com/loopnet/sale/searchByCity'

        headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': 'loopnet-api.p.rapidapi.com'
        }
        body = {
            'cityId': cityId
        }

        response = requests.post(listing_endpoint, headers=headers, json=body)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json().get('data', [])
        file_path = 'listings.json'

        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(
                f'File "{file_path}" created successfully with API response data.')

            return jsonify({
                'message': f'File "{file_path}" created successfully with API response data.'
            })

        except Exception as file_error:
            print("File already created")
            return jsonify({
                'message': f'File "{file_path}" created successfully with API response data.'
            })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching data from API: {e}'}), 500

    return jsonify(positions)


@app.route('/rent/details', methods=['GET'])
def get_rents_details():
    file_path = 'listings.json'
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)  # Load JSON data from the file
        folder_path = 'listingDetails'
        os.makedirs(folder_path, exist_ok=True)
        coor_map = {item['listingId']: item['coordinations'] for item in data}
        api_key = os.getenv('LOOP_API')
        listing_detail_endpoint = 'https://loopnet-api.p.rapidapi.com/loopnet/property/SaleDetails'
        headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': 'loopnet-api.p.rapidapi.com'
        }
        # sample size to get detail
        samples = data[:2]
        detail_listings_id_url = ""
        for i in range(len(samples)):
            listingId = samples[i]['listingId']
            print("listingId", listingId)
            file_path = f'listingDetails/listing_{listingId}.json'
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    pass
            body = {
                "listingId": listingId
            }
            response = requests.post(
                listing_detail_endpoint, headers=headers, json=body)
            response.raise_for_status()
            data = response.json().get('data', [])
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

        return jsonify({'info': "ok"})

    except FileNotFoundError:
        return jsonify({'error': f'The file "{file_path}" was not found.'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Failed to decode JSON from the file.'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


def fetch_competitor_restaurants(city, cuisine_type, price_level):
    # fetch all the competitors with the requesting user
    api_key = os.getenv('GOOGLE_MAP_API')
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    params = {
        'query': f'{cuisine_type} restaurants in {city}',
        'type': 'restaurant',
        'key': api_key
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])
    positions = []
    for result in results:
        if 'price_level' in result and result['price_level'] == price_level:
            position = {
                'lat': result['geometry']['location']['lat'],
                'lng': result['geometry']['location']['lng'],
            }
            positions.append(position)
    return positions


def fetch_neighborhood_populations(city):
    # fetch the population of each neighborhood in the given city
    client = Cerebras(
        api_key=os.getenv('CEREBRAS_API'))

    chat_completion = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[
            {"role": "user", "content": f"Generate a Python dictionary where the keys are the neighborhoods of {city} and the values are the population counts. Format the output as a valid Python dictionary.", }
        ],
    )

    # Extract and process the result
    result = chat_completion.choices[0].message.content.strip()
    # Fetch {...} part in the responded string
    match = re.findall(r'\{[^}]*\}', result)

    # evaluate as a dict
    neighborhood_populations = eval(match[0])
    return neighborhood_populations


if __name__ == '__main__':
    app.run(debug=True)
