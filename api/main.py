from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, 'models', '1.keras')                           
MODEL = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ['Early Blight','Late Blight','Healthy']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))

    img_batch = np.expand_dims(image, 0)

    predictions  = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image  = read_file_as_image(await file.read())
    return image

if __name__ == "__main__":
    uvicorn.run(app, host='localhost',port = 8000)