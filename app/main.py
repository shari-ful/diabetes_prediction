import os
from fastapi import FastAPI
from .schema import PredictSchema
import pickle
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'prediction-model.pkl')
CLASSIFIER = pickle.load(open(MODEL_DIR, 'rb'))



app = FastAPI(
    title='Diabetes Prediction API',
    description='Diabetes Prediction API')

@app.post('/predict', tags=['prediction'])
async def predict_diabetes(schema: PredictSchema):
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
        prediction = CLASSIFIER.predict(data)
        if prediction[0] == 0:
            status = 'Congratulation! You don\'t have diabetes'

        else:
            status = 'Oops! You have diabetes'

        return {"status": status}
    except:
        raise ValueError

    