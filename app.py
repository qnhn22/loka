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
import numpy as np
from models.weight_sum_op import WeightSumOptimization
from flask_cors import CORS
import pandas
load_dotenv()

app = Flask(__name__)
CORS(app)

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
        'total_distance_to_competitors': 0,
        'cost': 0,
        'population': 0,
    } for _ in rents]

    restaurants = list(fetch_restaurants(city, cuisine_type))
    competitors = []
    for res in restaurants:
        if res['price_level'] == int(price_level):
            competitors.append(res)

    metrics_coors = {}
    for i in range(len(rents)):
        r = rents[i]
        candidates[i]['total_distance_to_competitors'] = calculate_distance_competitors(
            (r['lng'], r['lat']), competitors)
        candidates[i]['cost'] = r['cost']
        candidates[i]['population'] = r['population']
        metrics_coors[(candidates[i]['total_distance_to_competitors'], candidates[i]['cost'], candidates[i]['population'])] = {
            'lng': r['lng'],
            'lat': r['lat'],
        }

    data = {
        'distance': [],
        'price': [],
        'population': []
    }
    for i in range(len(candidates)):
        data['distance'].append(candidates[i]['total_distance_to_competitors'])
        data['price'].append(candidates[i]['cost'])
        data['population'].append(candidates[i]['population'])

    w_s_op = WeightSumOptimization(data)
    rank = w_s_op.rank_data()

    ranked_candidates = [tuple(x) for x in rank.to_records(index=False)]
    locations = []

    thres = 10
    if len(ranked_candidates) < 10:
        thres = len(ranked_candidates)

    for i in range(thres):
        distance = ranked_candidates[i][0]
        cost = ranked_candidates[i][1]
        population = ranked_candidates[i][2]
        locations.append({
            'distance': int(distance),
            'cost': int(cost),
            'population': int(population),
            'lng': metrics_coors[(distance, cost, population)]['lng'],
            'lat': metrics_coors[(distance, cost, population)]['lat']
        })

    return jsonify(locations)


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

    for i in range(len(samples)):
        listingId = samples[i]['listingId']
        lng = samples[i]['coordinations'][0][0]
        lat = samples[i]['coordinations'][0][1]
        body = {
            "listingId": listingId
        }
        response = requests.post(
            listing_detail_endpoint, headers=headers, json=body)
        data = response.json().get('data', [])

        if not data:
            continue

        rents = []
        population = 5000
        zip_population = populations_db.find_one(
            {'zipcode': data[0]['location']['postalCode']})

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


def calculate_distance_competitors(coor, competitors):
    lng, lat = coor
    total_dist = 0
    for c in competitors:
        total_dist += math.sqrt((lng - c['lng'])**2 + (lat - c['lat'])**2)
    return total_dist


if __name__ == '__main__':
    app.run(debug=True)
