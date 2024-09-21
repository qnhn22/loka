from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

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
    
    positions = [{'lat': result['geometry']['location']['lat'], 'lng': result['geometry']['location']['lng']} for result in results]
    
    return jsonify(positions)

if __name__ == '__main__':
    app.run(debug=True)