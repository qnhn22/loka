import React, { useEffect, useState } from "react";
import Map from "../components/Map";
import Input from "../components/Input";
import { withRequiredAuthInfo } from "@propelauth/react";
import axios from "axios";
function HomePage() {
  const [showResults, toggleShowResults] = useState(true);
  const [city, setCity] = useState("");
  const [cuisine, setCuisine] = useState("");
  const [costLevel, setCostLevel] = useState("");
  const [rentBudget, setRentBudget] = useState("");
  const [locations, setLocations] = useState([]);
  useEffect(() => { 
    setLocations([
      {
        "cost": 2500,
        "distance": 0,
        "lat": 40.712776,
        "lng": -74.005974,
        "population": 5000
      },
      {
        "cost": 2700,
        "distance": 0,
        "lat": 40.713776,
        "lng": -74.004974,
        "population": 5000
      },])
  }, []);
  const inputStyle =
    "min-w-[100px] w-full p-2   border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500";
  const handleSubmit = (e) => {
    e.preventDefault();
    const searchParams = {
      city,
      cuisine,
      costLevel,
      rentBudget,
    };
    toggleShowResults(true);
    const endPoint = "YOUR_API_ENDPOINT";
    // axios
    //   .get(endPoint, {
    //     headers: searchParams,
    //   })
    //   .then((response) => {
    //     setLocations(response.data);
    //     toggleShowResults(true);
    //   })
    //   .catch((error) => {
    //     console.error('There was an error fetching the data!', error);
    //   });
  };

  return (
    <>
      <div className="flex ">
        <div className="w-[30%]">
          <>
            <div className="flex flex-col justify-start   gap-y-5 p-2   border-r-2  h-[100vh]">
              <input
                className={inputStyle}
                type="text"
                placeholder="City"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                required
              />
              <input
                className={inputStyle}
                type="text"
                placeholder="Cuisine Type"
                value={cuisine}
                onChange={(e) => setCuisine(e.target.value)}
                required
              />
              <input
                className={inputStyle}
                type="number"
                min={1}
                max={5}
                placeholder="Cost Level $$"
                value={costLevel}
                onChange={(e) => setCostLevel(e.target.value)}
                required
              />
              <input
                className={inputStyle}
                type="number"
                placeholder="Rent Budget"
                value={rentBudget}
                step={0.01}
                onChange={(e) => setRentBudget(e.target.value)}
                required
              />
              <button
                className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-300"
                type="submit"
                onClick={handleSubmit}
              >
                Find
              </button>
            </div>
          </>
        </div>
        {showResults ? (
        <>
          <div className="relative w-[25%] bg-opacity-50 bg-gray-200 p-4 text-lg">
            <button
              className="absolute top-0 right-0 m-2 cursor-pointer text-xl"
              onClick={() => { toggleShowResults(false) }}
            >
              X
            </button>
            {locations.map((location, index) => (
              <div key={index} className=" border-b-2 border-gray-400 mt-2 flex-col flex justify-start gap-x-3 p-3">
                <span><b>Cost:</b> {location.cost} $</span>
                <span><b>Population:</b> {location.population}</span>
                <span><b>Total Distance from competitors:</b> {location.distance}  </span>

              </div>
            ))}
          </div>
        </>
      ) : (
        <></>
      )}
      {showResults ?( <>
        <div className="w-[50%]">
          <Map locations={locations}/>
        </div>
      </>):<>
      
        <div className="w-[70%]">
          <Map locations={locations}/>
        </div>
      </>}
      </div>
    </>
  );
}

export default withRequiredAuthInfo(HomePage);
