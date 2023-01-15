import axios from "axios";
import React, { useEffect } from "react";

const Home = () => {
  useEffect(() => {
    axios.get("http://localhost:5000/api").then(console.log).catch(console.err);
  }, []);

  return <div>Home</div>;
};

export default Home;
