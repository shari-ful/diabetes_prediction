from fastapi import FastAPI
from .schema import PredictSchema
import pickle
import numpy as np


predict_model = 'prediction-model.pkl'
classifier = pickle.load(open(predict_model, 'rb'))


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
        prediction = classifier.predict(data)
        return prediction
    except:
        raise ValueError

    