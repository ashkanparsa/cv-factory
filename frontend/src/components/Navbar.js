
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-500 text-white py-4">
      <div className="container mx-auto flex justify-between">
        <h1 className="text-lg font-bold">My App</h1>
        <div>
          <Link to="/dashboard" className="px-4">
            Dashboard
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
        