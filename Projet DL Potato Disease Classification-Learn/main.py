from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

Model = tf.keras.models.load_model("../Models/2.keras")

class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

@app.get("/ping")
async def ping():
    return "hello"


def read_f_as_arr(data) ->np.ndarray:
    im = np.array(Image.open(BytesIO(data)))
    return im

@app.post("/predict")
async def prediction(file: UploadFile = File(...)):
    
    image_np  = read_f_as_arr(await file.read())
    img_red = np.expand_dims(image_np, axis=0)
    predictions = Model.predict(img_red)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class ": predicted_class, "confidence":float(confidence) }
