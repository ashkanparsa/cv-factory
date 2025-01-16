
import React from "react";
import { FaGoogle, FaMicrosoft, FaApple, FaFacebook, FaLinkedin } from "react-icons/fa";

const Login = () => {
  const handleLogin = (provider) => {
    window.location.href = `/auth/login/${provider}`;
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-green-500">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4 text-center text-gray-800">Welcome Back</h2>
        <p className="text-center text-gray-600 mb-6">Sign in to your account</p>
        <div className="space-y-4">
          <button
            onClick={() => handleLogin("google")}
            className="flex items-center justify-center w-full bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
          >
            <FaGoogle className="mr-2" /> Sign in with Google
          </button>
          <button
            onClick={() => handleLogin("microsoft")}
            className="flex items-center justify-center w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
          >
            <FaMicrosoft className="mr-2" /> Sign in with Microsoft
          </button>
          <button
            onClick={() => handleLogin("apple")}
            className="flex items-center justify-center w-full bg-black text-white py-2 px-4 rounded hover:bg-gray-800"
          >
            <FaApple className="mr-2" /> Sign in with Apple
          </button>
          <button
            onClick={() => handleLogin("facebook")}
            className="flex items-center justify-center w-full bg-blue-800 text-white py-2 px-4 rounded hover:bg-blue-900"
          >
            <FaFacebook className="mr-2" /> Sign in with Facebook
          </button>
          <button
            onClick={() => handleLogin("linkedin")}
            className="flex items-center justify-center w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
          >
            <FaLinkedin className="mr-2" /> Sign in with LinkedIn
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;
