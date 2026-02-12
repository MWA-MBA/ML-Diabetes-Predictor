# Quick Start Guide - GitHub & Render Deployment

## 📋 What's Been Set Up

✅ **Streamlit Application** - Interactive ML prediction UI (ml_app.py)
✅ **FastAPI REST API** - Production-grade API with Swagger docs (api_app.py)
✅ **Docker Support** - Multi-container setup with docker-compose
✅ **Production Dockerfile** - Optimized for Render deployment
✅ **Git Repository** - Already initialized with commits
✅ **Environment Config** - render.yaml for automatic Render deployment

---

## 🚀 Next Steps

### 1. Create GitHub Repository

Visit https://github.com/new and:
- Repository name: `ML-Diabetes-Predictor`
- Description: "ML Diabetes prediction service with FastAPI and Streamlit"
- Make it **Public** (for free Render deployment)
- Click "Create repository"

### 2. Update Git Remote (if needed)

If your GitHub URL is different:
```powershell
cd "c:\Users\windows 10\Desktop\ML Diabetetes Predictor"
git remote set-url origin https://github.com/YOUR_USERNAME/ML-Diabetes-Predictor.git
```

### 3. Push to GitHub

```powershell
cd "c:\Users\windows 10\Desktop\ML Diabetetes Predictor"
git push origin main
```

---

## 📱 What You Have

### Files Created:
- **api_app.py** - FastAPI application with endpoints
  - `GET /` - API info
  - `GET /health` - Health check
  - `POST /predict` - Single prediction
  - `POST /predict-batch` - Batch predictions
  - `GET /docs` - Swagger UI

- **Dockerfile** - FastAPI container (port 8000)
- **Dockerfile.streamlit** - Streamlit container (port 8501)
- **docker-compose.yml** - Local development setup
- **render.yaml** - Render deployment config
- **DEPLOYMENT.md** - Detailed documentation
- **.gitignore** - Proper Git ignore rules

---

## 🐳 Local Testing Before Deployment

### Run API Locally:
```powershell
uvicorn api_app:app --reload
```
Visit: http://localhost:8000/docs for interactive Swagger docs

### Run Streamlit Locally:
```powershell
streamlit run ml_app.py
```
Visit: http://localhost:8501

### Run Both with Docker Compose:
```powershell
docker-compose up
```

---

## ☁️ Deploy on Render.com

### Step 1: Setup Render Account
1. Go to https://render.com and sign up (connect your GitHub)
2. Create a new "Web Service"
3. Connect your GitHub repository

### Step 2: Configure Service
- Select `ML-Diabetes-Predictor` repo
- Branch: `main`
- Build command: (leave blank - uses Dockerfile)
- Start command: (leave blank - uses Dockerfile)
- Environment: `Docker`
- Region: `Ohio` (or your preference)
- Plan: `Free`

### Step 3: Deploy
- Click "Create Web Service"
- Render will automatically build and deploy
- Your API will be available at `https://your-render-url.onrender.com`

### Step 4: Test Deployment
```powershell
# Test health endpoint
curl https://your-render-url.onrender.com/health

# Test prediction
curl -X POST "https://your-render-url.onrender.com/predict" `
  -H "Content-Type: application/json" `
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

### Optional: Deploy Streamlit UI
Create another Web Service with:
- Same repository
- Build from: `Dockerfile.streamlit`
- This will run on port 8501

---

## 📊 API Usage Examples

### Python:
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "pregnancies": 3,
    "glucose": 117,
    "blood_pressure": 72,
    "skin_thickness": 29,
    "insulin": 125,
    "bmi": 32.3,
    "diabetes_pedigree_function": 0.3725,
    "age": 29
}
response = requests.post(url, json=data)
print(response.json())
```

### JavaScript/Node.js:
```javascript
const data = {
    pregnancies: 3,
    glucose: 117,
    blood_pressure: 72,
    skin_thickness: 29,
    insulin: 125,
    bmi: 32.3,
    diabetes_pedigree_function: 0.3725,
    age: 29
};

fetch('http://localhost:8000/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## 🔍 Troubleshooting

**Container won't start:**
- Check logs in Render dashboard
- Ensure model files (`best_xgb_weighted_model.joblib`, `scaler.joblib`) are tracked in Git

**Port conflicts locally:**
- FastAPI: 8000 → Change with `--port 8001`
- Streamlit: 8501 → Change with `--server.port 8502`

**Git push fails:**
- Verify remote URL: `git remote -v`
- Check authentication (may need GitHub token)

**Render deployment fails:**
- Ensure `.gitignore` doesn't exclude model files
- Check build logs in Render dashboard
- Verify `requirements.txt` has all dependencies

---

## 📝 Project Structure After Setup

```
ML-Diabetes-Predictor/
├── ml_app.py                       # Streamlit UI
├── api_app.py                      # FastAPI REST API ⭐
├── best_xgb_weighted_model.joblib  # ML Model
├── scaler.joblib                   # Data scaler
├── requirements.txt                # Python packages
├── Dockerfile                      # API container
├── Dockerfile.streamlit            # UI container
├── docker-compose.yml              # Local dev setup
├── render.yaml                     # Render deployment
├── DEPLOYMENT.md                   # Full documentation
├── README.md                       # Project info
├── .gitignore                      # Git ignore rules
└── Notebooks/
    └── Diabetes_ML+DL_Prediction_Tool.ipynb
```

---

## ✨ What's Different Now

| Component | Before | Now |
|-----------|--------|-----|
| UI | ✅ Streamlit | ✅ Streamlit + FastAPI REST API |
| API | ❌ None | ✅ Full-featured with Swagger |
| Docker | ✅ Basic | ✅ Production-ready with health checks |
| Deployment | ❌ Manual | ✅ Automated via Render.yaml |
| Documentation | Basic | ✅ Comprehensive (DEPLOYMENT.md) |
| Development | Single app | ✅ Local stack with docker-compose |

---

## 🎯 Summary

Your project is **production-ready**!

1. Create GitHub repo (free public)
2. Push code: `git push origin main`
3. Connect to Render.com → Auto-deploy on every push
4. Access API at: `https://your-render-url.onrender.com`
5. View Swagger docs: `https://your-render-url.onrender.com/docs`

All files are committed and ready. Just need the GitHub repository URL!
