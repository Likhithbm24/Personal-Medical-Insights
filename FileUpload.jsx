// src/components/FileUpload.jsx
import React, { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please choose a file.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:8000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
      alert("Failed to upload. Check backend.");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Lab Report</h2>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {response && (
        <div className="results">
          <h3>Extracted Data:</h3>
          <pre>{JSON.stringify(response.data, null, 2)}</pre>
          <h3>Interpretation:</h3>
          <pre>{JSON.stringify(response.explanation, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
