
import React, { useState } from "react";

const FileUpload = () => {
  const [files, setFiles] = useState([]);
  const [progress, setProgress] = useState(0);

  const handleFileChange = (e) => {
    setFiles([...e.target.files]);
  };

  const handleUpload = () => {
    // Simulate progress
    setProgress(50);
    setTimeout(() => setProgress(100), 2000);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-lg font-semibold mb-4 text-gray-800">Upload Files</h2>
      <div
        className="border-dashed border-2 border-gray-300 p-6 text-center rounded mb-4"
        onDragOver={(e) => e.preventDefault()}
      >
        Drag and Drop your files here or <input type="file" multiple onChange={handleFileChange} />
      </div>
      <button
        onClick={handleUpload}
        className="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600"
      >
        Upload
      </button>
      {progress > 0 && (
        <div className="mt-4">
          <div className="h-4 bg-gray-300 rounded">
            <div
              className="h-4 bg-green-500 rounded"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
          <p className="text-gray-600 mt-2">{progress}%</p>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
