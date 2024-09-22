import React, { useEffect } from 'react';
import { APIProvider, Map, Marker } from '@vis.gl/react-google-maps';
const GoogleMap = () => {
  const locations = []
  const key = "AIzaSyDpLOyGUc0JQH8U79KVMOnXbh1ZG57BnmE"
  const center = { lat: 40.712576, lng: -74.007474 }; // Adjust this to fit your use case

  return (
    <div className='h-screen w-full flex justify-center m-2'>
      <APIProvider apiKey={key}>
        <Map
          className='w-full h-full border-3 border-gray-100'
          defaultCenter={center}
          defaultZoom={18}
          gestureHandling={'greedy'}
          disableDefaultUI={true}

        >
          <Marker position={center} />
          {locations.map((location, index) => (
            <Marker
              key={index}
              position={{ lat: location.lat, lng: location.lng }}
            />
          ))}

        </Map>
      </APIProvider>
    </div>
  );
};

export default GoogleMap;