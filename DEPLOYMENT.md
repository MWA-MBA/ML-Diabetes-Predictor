# Development and Deployment Guide

## Project Structure

```
├── ml_app.py                    # Streamlit UI application
├── api_app.py                   # FastAPI REST API application
├── best_xgb_weighted_model.joblib  # Trained XGBoost model
├── scaler.joblib                # Data scaler for preprocessing
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Multi-service Docker image (default: FastAPI)
├── Dockerfile.streamlit         # Streamlit-specific Docker image
├── docker-compose.yml           # Local development setup
├── render.yaml                  # Render.com deployment configuration
└── README.md                    # Project documentation
```

## Local Development

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ML-Diabetes-Predictor
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

**Option 1: Streamlit UI**
```bash
streamlit run ml_app.py
```
Access at http://localhost:8501

**Option 2: FastAPI**
```bash
uvicorn api_app:app --reload
```
Access at http://localhost:8000
Swagger docs at http://localhost:8000/docs

**Option 3: Both with Docker Compose**
```bash
docker-compose up
```
- API: http://localhost:8000
- UI: http://localhost:8501

## Docker

### Build Images

FastAPI (default):
```bash
docker build -t diabetes-api .
```

Streamlit:
```bash
docker build -f Dockerfile.streamlit -t diabetes-ui .
```

### Run Containers

FastAPI:
```bash
docker run -p 8000:8000 diabetes-api
```

Streamlit:
```bash
docker run -p 8501:8501 diabetes-ui
```

## API Endpoints

All endpoints include Swagger documentation at `/docs`

- `GET /` - API information
- `GET /health` - Health check
- `POST /predict` - Single prediction
- `POST /predict-batch` - Batch predictions

### Example: Single Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 3,
    "glucose": 117,
    "blood_pressure": 72,
    "skin_thickness": 29,
    "insulin": 125,
    "bmi": 32.3,
    "diabetes_pedigree_function": 0.3725,
    "age": 29
  }'
```

## Deployment

### Render.com

1. Create a new Web Service on Render.com
2. Connect your GitHub repository
3. Use the provided `render.yaml` for configuration
4. Deploy will start automatically on push

The service includes:
- Automatic health checks at `/health`
- Environment variables configured
- Python 3.9 runtime
- Auto-restart on failure

### Environment Variables

For production deployment, ensure these are set:
- `PYTHONUNBUFFERED=1` (included in render.yaml)

## GitHub Integration

### Initial Setup

```bash
git init
git add .
git commit -m "Initial commit: Diabetes ML Predictor with FastAPI and Streamlit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### Deployment

Every push to the `main` branch will trigger automatic deployment on Render.com.

## Model Details

- **Algorithm**: XGBoost with weighted classification
- **Features**: 8 patient health metrics
- **Accuracy**: Based on Pima Indians Diabetes Dataset
- **Input Range**: Validated within realistic medical ranges

## API Request/Response Format

### Request
```json
{
  "pregnancies": 3,
  "glucose": 117,
  "blood_pressure": 72,
  "skin_thickness": 29,
  "insulin": 125,
  "bmi": 32.3,
  "diabetes_pedigree_function": 0.3725,
  "age": 29
}
```

### Response
```json
{
  "prediction": 1,
  "probability_diabetes": 0.75,
  "probability_no_diabetes": 0.25
}
```

## Support & Monitoring

- **Health Check**: `GET /health` endpoint
- **API Documentation**: Swagger at `/docs`
- **Logs**: Check Render.com dashboard for deployment logs
- **Performance**: Monitor response times via Render.com metrics
