import React, { useEffect ,useState} from 'react';
import { APIProvider, Map, Marker,InfoWindow  } from '@vis.gl/react-google-maps';
const GoogleMap = ({locations}) => {
  const [selectedMarker, setSelectedMarker] = useState(null);
  const key = "AIzaSyDpLOyGUc0JQH8U79KVMOnXbh1ZG57BnmE"
  const center = { lat: 40.712576, lng: -74.007474 }; // Adjust this to fit your use case
  const handleMarkerClick = (location) => {
    setSelectedMarker(location);
  };

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
          {locations&&locations.map((location, index) => (
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