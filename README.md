# Diabetes Prediction ML App

A machine learning application for diabetes prediction built with Streamlit, using XGBoost with a weighted model.

## Features

- Interactive Streamlit web interface
- XGBoost ML model for diabetes prediction
- User-friendly sliders for input features
- Probability-based predictions
- Containerized with Docker for easy deployment

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ML-Diabetes-Predictor.git
cd ML-Diabetes-Predictor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run ml_app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Docker

Build and run locally:
```bash
docker build -t diabetes-predictor .
docker run -p 8501:8501 diabetes-predictor
```

### Render Deployment

1. Push your code to GitHub

2. Go to [Render Dashboard](https://dashboard.render.com)

3. Click "New +" → "Web Service"

4. Connect your GitHub repository

5. Configure:
   - **Name:** diabetes-predictor
   - **Environment:** Docker
   - **Region:** Ohio (or your preferred region)
   - **Plan:** Free (or paid for production)

6. Click "Create Web Service"

Render will automatically build and deploy your app from the Dockerfile.

## Project Files

- `ml_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `best_xgb_weighted_model.joblib` - Trained XGBoost model
- `scaler.joblib` - Feature scaler
- `Dockerfile` - Docker configuration
- `render.yaml` - Render deployment configuration

## Model Details

The model predicts diabetes based on 8 input features:
- Pregnancies
- Glucose level
- Blood Pressure
- Skin Thickness
- Insulin level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

## Requirements

- Python 3.9+
- See `requirements.txt` for full dependencies
