import { useState } from "react";
const Input=()=>{
    const [city, setCity] = useState("");
    const [cuisine, setCuisine] = useState("");
    const [costLevel, setCostLevel] = useState("");
    const [rentBudget, setRentBudget] = useState("");
    const inputStyle =
      "min-w-[100px] w-full p-2   border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500";
    const handleSubmit = () => {
      const searchParams = {
        city,
        cuisine,
        costLevel,
        rentBudget,
      };
      // navigate('/results', { state: searchParams });
    };
  return (
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
          >
            Find
          </button>
    </div>
    </>
  )
}
export default Input;