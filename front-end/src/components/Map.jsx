import React, { useEffect, useState } from 'react';
import { APIProvider, Map, Marker, InfoWindow } from '@vis.gl/react-google-maps';
const GoogleMap = ({ locations }) => {
  const [selectedMarker, setSelectedMarker] = useState(null);
  const [topLocations, setTopLocations] = useState(locations);
  const key = "AIzaSyDpLOyGUc0JQH8U79KVMOnXbh1ZG57BnmE"
  const [center, setCenter] = useState({ lat: 33, lng: -118 })  // Adjust this to fit your use case
  const handleMarkerClick = (location) => {
    setSelectedMarker(location);
  };
  console.log(locations);

  useEffect(() => {
    if (locations !== null & locations.length > 0) {
      setCenter({ lat: locations[0].lat, lng: locations[0].lng })
    }
    setTopLocations(locations)
  }, [locations.length])
  console.log(locations);
  console.log(center);

  return (
    <div className='h-screen w-full flex justify-center m-2'>
      <APIProvider apiKey={key}>
        <Map
          className='w-full h-full border-3 border-gray-100'
          defaultCenter={center}
          defaultZoom={10}
          gestureHandling={'greedy'}
          disableDefaultUI={true}

        >
          <Marker position={center} />
          {topLocations && topLocations.map((location, index) => (
            <Marker
              key={index}
              position={{ lat: location.lat, lng: location.lng }}
              onClick={() => handleMarkerClick(location)}
            />
          ))}

          {selectedMarker && (
            <InfoWindow
              position={selectedMarker}
              onCloseClick={() => setSelectedMarker(null)}
            >
              <div className=' flex flex-col'>
                <p>Location Info</p>
                <span><b>Cost:</b> {selectedMarker.cost} $ </span>
                <span><b>Population:</b> {selectedMarker.population}  </span>
                <span><b>Total Distance from competitors:</b> {selectedMarker.distance}  </span>
              </div>
            </InfoWindow>
          )}
        </Map>
      </APIProvider>
    </div>
  );
};

export default GoogleMap;