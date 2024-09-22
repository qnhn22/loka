from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
import json
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
import math
from urllib.parse import quote_plus
import certifi
from cerebras.cloud.sdk import Cerebras
import re
import os
import time
import random
load_dotenv()

app = Flask(__name__)

mongo_uri = f"{os.getenv('MONGO_URI')}&tlsCAFile={quote_plus(certifi.where())}"
client = MongoClient(mongo_uri, server_api=ServerApi(
    version="1", strict=True, deprecation_errors=True))
db = client['loka']
restaurants_db = db['restaurant']
rents_db = db['rent']
populations_db = db['population']


@app.route('/', methods=['GET'])
def find_best_locations():
    city = request.args.get('city')
    cuisine_type = request.args.get('cuisine_type')
    price_level = request.args.get('price_level')
    rents = fetch_rents(city)
    candidates = [{
        'id': '',
        'total_distance_to_competitors': 0,
        'cost': 0,
        ' population': 0,
    } for _ in rents]

    for i in range(len(rents)):
        r = rents[i]
        candidates[i]['id'] = r['listingId']
        candidates[i]['total_distance_to_competitiors'] = calculate_distance_competitors(
            (r['lng'], r['lat']), city, cuisine_type, price_level)
        candidates[i]['cost'] = r['cost']
        candidates[i]['population'] = r['population']

    # rank and return coordinates


def fetch_rents(city):
    rents = list(rents_db.find({'city': city}))
    if rents:
        return rents

    api_key = os.getenv('LOOP_API')
    listing_endpoint = 'https://loopnet-api.p.rapidapi.com/loopnet/sale/searchByCity'

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': 'loopnet-api.p.rapidapi.com'
    }
    body = {
        'city': city
    }

    res = requests.post(listing_endpoint, headers=headers, json=body)

    rentsData = res.json().get('data', [])
    listing_detail_endpoint = 'https://loopnet-api.p.rapidapi.com/loopnet/property/SaleDetails'
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': 'loopnet-api.p.rapidapi.com'
    }

    samples = rentsData[:20]
    print(samples)

    for i in range(len(samples)):
        listingId = samples[i]['listingId']
        lng = samples[i]['coordinations'][0][0]
        lat = samples[i]['coordinations'][0][1]
        print("listingId", listingId)
        body = {
            "listingId": listingId
        }
        response = requests.post(
            listing_detail_endpoint, headers=headers, json=body)
        data = response.json().get('data', [])
        print("kekekekekekek")
        file_path = 'listings.json'
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        if not data:
            continue

        print("kekekekekekek")

        rents = []
        population = 5000
        zip_population = populations_db.find_one(
            {'zipcode': data[0]['location']['postalCode']})
        print(zip_population)
        if zip_population:
            population = zip_population['population']

        rent = {
            'listingId': listingId,
            'lng': lng,
            'lat': lat,
            'city': city,
            'cost': random.randint(2000, 4000),
            'population': population
        }

        rents.append(rent)
        rents_db.insert_one(rent)

    return res


def fetch_restaurants(city, cuisine_type):
    query = {
        "city": city,
        "cuisine_type": cuisine_type,
    }

    print("hello world")

    # check whether cuisine_type restaurants from city have been fetch from API,
    restaurants = list(restaurants_db.find(query, {"_id": 0}))
    if restaurants:
        return restaurants

    api_key = os.getenv('GOOGLE_MAP_API')
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    params = {
        'query': f'{cuisine_type} restaurants in {city}',
        'type': 'restaurant',
        'key': api_key
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])
    restaurants = []
    for result in results:
        if 'price_level' in result:
            r = {
                'city': city,
                'cuisine_type': cuisine_type,
                'price_level': result['price_level'],
                'lng': result['geometry']['location']['lng'],
                'lat': result['geometry']['location']['lat'],
            }
            restaurants_db.insert_one(r)
            restaurants.append(r)
    return restaurants


def calculate_distance_competitors(coor, city, cuisine_type, price_level):
    query = {
        'city': city,
        'cuisine_type': cuisine_type,
        'price_level': price_level
    }
    competitors = list(restaurants_db.find(query, {query}))
    lng, lat = coor
    total_dist = 0
    for c in competitors:
        total_dist += math.sqrt((lng - c['lng'])**2 + (lat - c['lat'])**2)
    return total_dist


# def fetch_neighborhood_populations(city):
#     # fetch the population of each neighborhood in the given city
#     client = Cerebras(
#         api_key=os.getenv('CEREBRAS_API'))

#     chat_completion = client.chat.completions.create(
#         model="llama3.1-8b",
#         messages=[
#             {"role": "user", "content": f"Generate a Python dictionary where the keys are the neighborhoods of {city} and the values are the population counts. Format the output as a valid Python dictionary without any comment.", }
#         ],
#     )

#     # Extract and process the result
#     result = chat_completion.choices[0].message.content.strip()
#     # Fetch {...} part in the responded string
#     match = re.findall(r'\{[^}]*\}', result)

#     input = {
#         'city': city,
#         'pop': neighborhood_populations
#     }
#     neighborhoods_db.insert_one(input)

#     return neighborhood_populations


if __name__ == '__main__':
    app.run(debug=True)
