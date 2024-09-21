import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { APIProvider, Map, Marker } from '@vis.gl/react-google-maps';

function ResultsPage() {
  const { state } = useLocation();
  // const [locations, setLocations] = useState([]);

  // useEffect(() => {
  //   const fetchLocations = async () => {
  //     const response = await fetch('/api/locations', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json'
  //       },
  //       body: JSON.stringify(state)
  //     });
  //     const data = await response.json();
  //     setLocations(data);
  //   };
  //   fetchLocations();
  // }, [state]);

  const locations = [
    {
      "name": "Bistro Paris",
      "address": "123 Main St, Downtown, Cityville",
      "rent": 4500,
      "population_density": 12000,
      "lat": 40.712776,
      "lng": -74.005974
    },
    {
      "name": "Sushi Zen",
      "address": "456 Elm St, Midtown, Cityville",
      "rent": 4000,
      "population_density": 15000,
      "lat": 40.713776,
      "lng": -74.002974
    },
    {
      "name": "Pizza Bella",
      "address": "789 Maple Ave, Eastside, Cityville",
      "rent": 3800,
      "population_density": 10000,
      "lat": 40.715776,
      "lng": -74.009974
    },
    {
      "name": "Taco Loco",
      "address": "101 Oak St, Westside, Cityville",
      "rent": 3200,
      "population_density": 9000,
      "lat": 40.711776,
      "lng": -74.007974
    },
    // {
    //   "name": "Curry Palace",
    //   "address": "202 Pine St, Uptown, Cityville",
    //   "rent": 3600,
    //   "population_density": 13000,
    //   "lat": 40.713576,
    //   "lng": -74.004974
    // },
    // {
    //   "name": "Burger Joint",
    //   "address": "303 Cedar Ave, Downtown, Cityville",
    //   "rent": 5000,
    //   "population_density": 16000,
    //   "lat": 40.712176,
    //   "lng": -74.006874
    // },
    // {
    //   "name": "Pasta La Vista",
    //   "address": "404 Birch St, Midtown, Cityville",
    //   "rent": 4200,
    //   "population_density": 11000,
    //   "lat": 40.714576,
    //   "lng": -74.008974
    // },
    // {
    //   "name": "Grill & Chill",
    //   "address": "505 Chestnut St, Eastside, Cityville",
    //   "rent": 3500,
    //   "population_density": 9500,
    //   "lat": 40.715976,
    //   "lng": -74.010974
    // },
    // {
    //   "name": "Pho Delight",
    //   "address": "606 Walnut St, Westside, Cityville",
    //   "rent": 3700,
    //   "population_density": 10500,
    //   "lat": 40.712576,
    //   "lng": -74.007474
    // },
    // {
    //   "name": "Dim Sum Heaven",
    //   "address": "707 Spruce St, Uptown, Cityville",
    //   "rent": 3900,
    //   "population_density": 12500,
    //   "lat": 40.714176,
    //   "lng": -74.003974
    // }
  ];

  const center = { lat: 40.712576, lng: -74.007474 }; // Adjust this to fit your use case

  return (
    <div>
      <h1>Top 10 Locations</h1>
      <ul>
        {locations.map((location, index) => (
          <li key={index}>
            {location.name} - {location.address} - Rent: {location.rent}
          </li>
        ))}
      </ul>

      <div style={{ height: '400px', weight: '600px' }}>
        <APIProvider apiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
          <Map
            style={{ width: '200vw', height: '50vh' }}
            defaultCenter={center}
            defaultZoom={18}
            gestureHandling={'greedy'}
            disableDefaultUI={true}
          >
            {locations.map((location, index) => (
              <Marker
                key={index}
                position={{ lat: location.lat, lng: location.lng }}
              />
            ))}
          </Map>
        </APIProvider>
      </div>
    </div>
  );
}

// const Marker = ({ }) => <div>kakak</div>;

export default ResultsPage;
