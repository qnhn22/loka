import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// import './Home.css';

function HomePage() {
  const [city, setCity] = useState('');
  const [cuisine, setCuisine] = useState('');
  const [costLevel, setCostLevel] = useState('');
  const [rentBudget, setRentBudget] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const searchParams = {
      city,
      cuisine,
      costLevel,
      rentBudget
    };
    navigate('/results', { state: searchParams });
  };

  return (
    <div>
      <h1>Find the Best Locations to open Your F&B Business</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="City" value={city} onChange={(e) => setCity(e.target.value)} required />
        <input type="text" placeholder="Cuisine Type" value={cuisine} onChange={(e) => setCuisine(e.target.value)} required />
        <input type="number" min={1} max={5} placeholder="Cost Level" value={costLevel} onChange={(e) => setCostLevel(e.target.value)} required />
        <input type="number" placeholder="Rent Budget" value={rentBudget} step={0.01} onChange={(e) => setRentBudget(e.target.value)} required />
        <button type="submit">Find</button>
      </form>
    </div>
  );
}

export default HomePage;
