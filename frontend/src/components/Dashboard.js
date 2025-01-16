
import React from "react";
import Profile from "./Profile";
import FileUpload from "./FileUpload";

const Dashboard = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Profile />
        <div className="col-span-2">
          <FileUpload />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
