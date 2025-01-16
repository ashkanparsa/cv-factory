
import React from "react";

const Profile = () => {
  const profile = {
    fullName: "John Doe",
    email: "john.doe@example.com",
    profilePicture: "https://via.placeholder.com/150",
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md text-center">
      <img
        src={profile.profilePicture}
        alt="Profile"
        className="w-32 h-32 rounded-full mx-auto mb-4"
      />
      <h2 className="text-lg font-semibold text-gray-800">{profile.fullName}</h2>
      <p className="text-gray-600">{profile.email}</p>
    </div>
  );
};

export default Profile;
