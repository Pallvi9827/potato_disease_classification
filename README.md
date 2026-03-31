# Potato Disease Classification Web App

This is a full-stack machine learning web application that classifies potato leaf diseases from images using a deep learning model.  
The application allows users to upload a leaf image and get the predicted disease and confidence score.

---

## Tech Stack
- TensorFlow / Keras – Model training and prediction
- FastAPI – Backend API
- React – Frontend user interface
- Python
- JavaScript
- Git & GitHub

---

## Features
- Upload potato leaf image
- Predict disease class
- Show confidence score
- Image preview before prediction
- Full stack ML application
- REST API backend
- React frontend

---

## Disease Classes
- Early Blight
- Late Blight
- Healthy

---

## Project Structure

potato_disease/
├── api/                # FastAPI backend
│   ├── main.py
│   └── requirements.txt
│
├── frontend/           # React frontend
│   ├── public/
│   ├── src/
│   └── package.json
│
├── models/             # Trained model
│   └── 1.keras
│
├── Training/           # Model training notebook
│   └── training_model.ipynb
│
├── README.md
└── .gitignore

---

## How It Works
1. User uploads a potato leaf image in the React frontend
2. React sends the image to FastAPI backend
3. FastAPI loads the trained TensorFlow model
4. Model predicts the disease class
5. Backend returns prediction and confidence
6. React displays the result

---

## Run Backend
```bash
cd api
conda activate potato
uvicorn main:app --reload
```

## Run Frontend
```bash
cd frontend
npm start
```
## API Endpoint

#### POST /predict

Upload an image and get prediction:

Example response:
```json
{
  "class": "Early Blight",
  "confidence": 0.99
}
```
## Project Status

	•	Model training completed
	•	FastAPI backend completed
	•	React frontend completed
	•	Frontend connected to backend
	•	Local prediction working
	•	Ready for deployment

## Author

Pallvi.....
Machine Learning / AI Student