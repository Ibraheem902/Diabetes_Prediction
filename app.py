from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from predictor import DiabetesPredictor

app = FastAPI(
    title="Diabetes Prediction API",
    description="An API for predicting diabetes based on input features."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = DiabetesPredictor()

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/api/predict")
def predict_diabetes(data: PatientData):
    try:
        features = [
            data.Pregnancies,
            data.Glucose,
            data.BloodPressure,
            data.SkinThickness,
            data.Insulin,
            data.BMI,
            data.DiabetesPedigreeFunction,
            data.Age
        ]
        
        result = predictor.predict(features)
        
        return{
            'status': 'success',
            'data': result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))