import os
from fastapi import FastAPI
from .schema import PredictSchema
import pickle
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'prediction-model.pkl')
CLASSIFIER = pickle.load(open(MODEL_DIR, 'rb'))


app = FastAPI()

@app.post('/predict')
def predict_diabetes(schema: PredictSchema):
    preg = schema.preg
    glucose = schema.glucose
    bp = schema.bp
    st = schema.st
    insulin = schema.insulin
    bmi = schema.bmi
    dpf = schema.dpf
    age = schema.age

    data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    
    try:
        prediction = CLASSIFIER.predict_diabetes(data)
        return prediction
    except:
        raise ValueError

    