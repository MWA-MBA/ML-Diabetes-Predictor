# 🏥 ML Diabetes Predictor

A production-ready machine learning application for diabetes risk prediction using XGBoost classification. Deploy in minutes with Streamlit UI and Docker.

## 🎯 Key Features

- **Interactive Web UI** - Built with Streamlit for intuitive patient data input
- **ML Model** - XGBoost classifier trained on Pima Indians Diabetes Dataset
- **Instant Predictions** - Real-time risk assessment with probability scores
- **Docker Ready** - Containerized for consistent local & cloud deployment
- **Cloud Deployment** - One-click deployment to Render.com
- **Production Grade** - Health checks, validation, error handling

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/ML-Diabetes-Predictor.git
cd ML-Diabetes-Predictor
pip install -r requirements.txt
streamlit run ml_app.py
```

Open browser to `http://localhost:8501`

## 📊 Prediction Features

Predicts diabetes risk based on:
- **Pregnancies** - Number of pregnancies
- **Glucose** - Plasma glucose concentration
- **Blood Pressure** - Diastolic blood pressure (mm Hg)
- **Skin Thickness** - Triceps skin fold thickness (mm)
- **Insulin** - 2-Hour serum insulin (mu U/ml)
- **BMI** - Body Mass Index (weight in kg/(height in m)²)
- **Diabetes Pedigree Function** - Genetic predisposition score
- **Age** - Age in years

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t diabetes-predictor .
```

### Run Container
```bash
docker run -p 8501:8501 diabetes-predictor
```

Access at `http://localhost:8501`

## ☁️ Deploy to Render.com

### Quick Setup
1. Push code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click "New +" → "Web Service"
4. Connect this repository
5. Configure:
   - **Environment:** Docker
   - **Region:** Ohio (or your preference)
   - **Plan:** Free tier available
6. Click "Create Web Service"

Render automatically builds and deploys from the Dockerfile. Your app will be live in minutes!

## 📁 Project Structure

```
├── ml_app.py                          # Streamlit web application
├── best_xgb_weighted_model.joblib     # Trained XGBoost model
├── scaler.joblib                      # Data preprocessing scaler
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Container configuration
├── render.yaml                        # Render.com deployment config
├── diabetes_pima.csv                  # Training dataset
└── README.md                          # Documentation
```

## 🔧 Technologies Used

- **Machine Learning:** XGBoost, scikit-learn, imbalanced-learn
- **Web Framework:** Streamlit
- **Deployment:** Docker, Render.com
- **Data Processing:** pandas, joblib
- **Python:** 3.9+

## 📦 Installation

### Requirements
- Python 3.9 or higher
- pip or conda

### Local Development

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ML-Diabetes-Predictor.git
cd ML-Diabetes-Predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run ml_app.py
```

## 📊 Model Performance

- **Algorithm:** XGBoost with class weighting
- **Dataset:** Pima Indians Diabetes Database
- **Input Features:** 8 medical measurements
- **Output:** Binary classification (0 = No Diabetes, 1 = Diabetes)

## 🎨 User Interface

The Streamlit app provides:
- Interactive sliders for all 8 input features
- Real-time prediction with confidence scores
- Color-coded results (green = low risk, red = high risk)
- Responsive design for desktop and mobile

## 🔒 Privacy & Security

- Model runs locally in your container
- No data sent to external servers
- Predictions computed on your infrastructure

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Ready to deploy?** Push to GitHub and connect to Render.com for automatic deployment! 🚀
