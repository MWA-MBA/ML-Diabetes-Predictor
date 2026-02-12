from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import os
from typing import List

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Prediction API",
    description="ML API for diabetes prediction using XGBoost model",
    version="1.0.0"
)

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained ML model and scaler
try:
    best_ml_model = joblib.load(os.path.join(BASE_DIR, "best_xgb_weighted_model.joblib"))
    scaler = joblib.load(os.path.join(BASE_DIR, "scaler.joblib"))
except FileNotFoundError as e:
    raise RuntimeError(f"Error loading model files: {e}")


# Define request/response models
class DiabetesPredictionRequest(BaseModel):
    """Request model for diabetes prediction"""
    pregnancies: float = Field(..., ge=0, le=17, description="Number of pregnancies")
    glucose: float = Field(..., ge=44, le=199, description="Plasma glucose concentration")
    blood_pressure: float = Field(..., ge=24, le=122, description="Diastolic blood pressure (mm Hg)")
    skin_thickness: float = Field(..., ge=7, le=99, description="Triceps skin fold thickness (mm)")
    insulin: float = Field(..., ge=14, le=846, description="2-Hour serum insulin (mu U/ml)")
    bmi: float = Field(..., ge=18.2, le=67.1, description="Body mass index (weight in kg/(height in m)^2)")
    diabetes_pedigree_function: float = Field(..., ge=0.078, le=2.42, description="Diabetes pedigree function")
    age: float = Field(..., ge=21, le=81, description="Age (years)")

    class Config:
        schema_extra = {
            "example": {
                "pregnancies": 3,
                "glucose": 117,
                "blood_pressure": 72,
                "skin_thickness": 29,
                "insulin": 125,
                "bmi": 32.3,
                "diabetes_pedigree_function": 0.3725,
                "age": 29
            }
        }


class DiabetesPredictionResponse(BaseModel):
    """Response model for diabetes prediction"""
    prediction: int = Field(..., description="Prediction: 0 = No diabetes, 1 = Diabetes")
    probability_diabetes: float = Field(..., ge=0, le=1, description="Probability of diabetes")
    probability_no_diabetes: float = Field(..., ge=0, le=1, description="Probability of no diabetes")


class BatchPredictionRequest(BaseModel):
    """Request model for batch predictions"""
    predictions: List[DiabetesPredictionRequest]


class BatchPredictionResponse(BaseModel):
    """Response model for batch predictions"""
    results: List[DiabetesPredictionResponse]


@app.get("/", tags=["Info"])
def read_root():
    """Root endpoint - API information"""
    return {
        "message": "Diabetes Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {
        "status": "healthy",
        "model_loaded": best_ml_model is not None,
        "scaler_loaded": scaler is not None
    }


@app.post("/predict", response_model=DiabetesPredictionResponse, tags=["Predictions"])
def predict_diabetes(request: DiabetesPredictionRequest):
    """
    Make a diabetes prediction for a single patient.
    
    Returns prediction (0 or 1) and probability of diabetes.
    """
    try:
        # Create a DataFrame from the request
        input_data = pd.DataFrame([{
            'Pregnancies': request.pregnancies,
            'Glucose': request.glucose,
            'BloodPressure': request.blood_pressure,
            'SkinThickness': request.skin_thickness,
            'Insulin': request.insulin,
            'BMI': request.bmi,
            'DiabetesPedigreeFunction': request.diabetes_pedigree_function,
            'Age': request.age
        }])

        # Scale the input data
        scaled_input_data = scaler.transform(input_data)

        # Make prediction
        prediction = best_ml_model.predict(scaled_input_data)[0]
        prediction_proba = best_ml_model.predict_proba(scaled_input_data)[0]

        return DiabetesPredictionResponse(
            prediction=int(prediction),
            probability_diabetes=float(prediction_proba[1]),
            probability_no_diabetes=float(prediction_proba[0])
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")


@app.post("/predict-batch", response_model=BatchPredictionResponse, tags=["Predictions"])
def predict_batch(request: BatchPredictionRequest):
    """
    Make diabetes predictions for multiple patients in batch.
    
    Returns list of predictions with probabilities.
    """
    try:
        results = []
        for patient in request.predictions:
            input_data = pd.DataFrame([{
                'Pregnancies': patient.pregnancies,
                'Glucose': patient.glucose,
                'BloodPressure': patient.blood_pressure,
                'SkinThickness': patient.skin_thickness,
                'Insulin': patient.insulin,
                'BMI': patient.bmi,
                'DiabetesPedigreeFunction': patient.diabetes_pedigree_function,
                'Age': patient.age
            }])

            scaled_input_data = scaler.transform(input_data)
            prediction = best_ml_model.predict(scaled_input_data)[0]
            prediction_proba = best_ml_model.predict_proba(scaled_input_data)[0]

            results.append(DiabetesPredictionResponse(
                prediction=int(prediction),
                probability_diabetes=float(prediction_proba[1]),
                probability_no_diabetes=float(prediction_proba[0])
            ))

        return BatchPredictionResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Batch prediction error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
