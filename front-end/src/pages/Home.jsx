import React, { useState } from "react";
import Map from "../components/Map";
import Input from "../components/Input";
function HomePage() {
 
  return (
    <>
      <div className="flex ">
        <div className="w-[20%]">

      <Input/>
        </div>
        <div className="w-[80%]">
      <Map/>
          </div>
      </div>
    </>
  );
}

export default HomePage;
