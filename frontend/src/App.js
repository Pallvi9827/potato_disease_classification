import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    setImagePreview(URL.createObjectURL(selectedFile));
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="App">
      <h1>Potato Disease Classifier</h1>

      <input type="file" onChange={handleFileChange} />
      <br /><br />

      {imagePreview && (
        <img src={imagePreview} alt="preview" width="300" />
      )}

      <br /><br />

      <button onClick={handleUpload}>Predict</button>

      <br /><br />

      {result && (
  <div className="result">
    <h2 style={{ color: result.class === "Healthy" ? "green" : "red" }}>
      Prediction: {result.class}
    </h2>
    <h3>Confidence: {(result.confidence * 100).toFixed(2)}%</h3>
  </div>
)}
    </div>
  );
}

export default App;