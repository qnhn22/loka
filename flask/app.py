from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API!'})
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    city = request.args.get('city')
    food_type = request.args.get('food_type')
    radius = request.args.get('radius')
    api_key = os.getenv('GOOGLE_MAP_API')
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    
    params = {
        'query': f'{food_type} restaurant in {city}',
        'radius': radius,
        'type': 'restaurant',
        'key': api_key
    }
    
    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])
    positions = []
    for result in results:
        position = {
            'lat': result['geometry']['location']['lat'],
            'lng': result['geometry']['location']['lng'],
            'price_level': result.get('price_level', 'N/A')
        }
        positions.append(position)    
    return jsonify(positions)

@app.route('/rent/listing', methods=['GET'])
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
            print(f'File "{file_path}" created successfully with API response data.')
            
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
        samples=data[:2]
        detail_listings_id_url=""
        for i in range(len(samples)) :
            listingId = samples[i]['listingId']
            file_path=f'listingDetails/listing_{listingId}.json'
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    pass
            body = {
            "listingId":listingId
                }
            response = requests.post(listing_detail_endpoint, headers=headers, json=body)
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
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')