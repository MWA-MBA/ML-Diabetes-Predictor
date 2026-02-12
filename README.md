# 🩺 Diabetes Risk Prediction System (Machine Learning)

## End-to-End Healthcare AI System Using XGBoost

## 📌 Overview

This project presents a production-ready Machine Learning system for predicting diabetes risk using structured clinical data.

The objective was to build a robust and clinically meaningful prediction system that prioritizes **Recall (Sensitivity)** to minimize missed diagnoses.

The final deployed model is:

> **XGBoost with Class-Weighted Learning**

The system includes:

* Data preprocessing pipeline
* Class imbalance handling
* Hyperparameter tuning with cross-validation
* Model evaluation using healthcare-relevant metrics
* Streamlit web application
* FastAPI REST API
* Docker containerization
* Cloud deployment on Render

## 🎯 Clinical Motivation

Early detection of diabetes is critical in preventing severe complications such as:

* Cardiovascular disease
* Kidney failure
* Neuropathy
* Vision loss

In healthcare screening systems:

* False Negatives = Missed diagnosis
* Missed diagnosis = Potential patient harm

Therefore, **Recall was prioritized over Accuracy** during model selection.

## 📊 Dataset

* Structured clinical dataset
* Binary target variable (0 = No Diabetes, 1 = Diabetes)
* Imbalanced class distribution
* Contains demographic and metabolic health indicators

## ⚙️ Data Preprocessing

### ✔ Missing Value Handling

Certain biologically implausible zeros were treated as missing and imputed using the median.

### ✔ Feature Scaling

StandardScaler was applied to normalize numerical features.

### ✔ Train/Validation/Test Split

Stratified 70/15/15 split to preserve class distribution.

### ✔ Data Leakage Prevention

All preprocessing steps were applied correctly to avoid leakage into validation and test sets.

## ⚖️ Handling Class Imbalance

Three techniques were evaluated:

* SMOTE
* Random Undersampling
* Class-Weighted Learning

The final selected strategy was:

> **Class-Weighted Learning with XGBoost**

This approach preserved original data structure while improving sensitivity to minority cases.

## 🧠 Model Development

Models evaluated:

* Logistic Regression
* Random Forest
* XGBoost

Hyperparameter tuning was performed using GridSearchCV with **Recall as the primary scoring metric**.

## 🏆 Final Model

### XGBoost (Class-Weighted)

### Why Selected:

* Highest Recall
* Strong ROC-AUC
* Effective modeling of nonlinear feature interactions
* Robust performance on structured tabular data

## 📈 Evaluation Metrics

Primary Metric:

* **Recall (Sensitivity)**

Secondary Metric:

* ROC-AUC

Accuracy was not prioritized due to class imbalance and clinical risk considerations.

## 🧪 Example Prediction

### API Endpoint

```
POST /predict
```

### Example Input

```json
{
  "Pregnancies": 2,
  "Glucose": 140,
  "BloodPressure": 80,
  "SkinThickness": 25,
  "Insulin": 100,
  "BMI": 30.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 45
}
```

### Example Output

```json
{
  "diabetes_risk_probability": 0.78,
  "high_risk": true
}
```

## 🚀 Deployment

### 🌐 Streamlit Web App

Interactive user interface for manual patient data entry.

### ⚡ FastAPI Backend

REST API with Swagger documentation for integration into external systems.

### 🐳 Docker

Fully containerized for reproducibility and portability.

### ☁️ Cloud Deployment

Hosted on Render (free tier).

## 📂 Repository Structure

```
├── ml_app.py
├── api.py
├── best_ml_model.pkl
├── scaler.pkl
├── requirements.txt
├── Dockerfile
├── Dockerfile.api
└── README.md
```

## ⚖️ Ethical Considerations

* Model supports clinicians, does not replace them.
* Dataset may contain demographic bias.
* External validation required before real-world clinical use.
* Continuous monitoring required to detect model drift.

## 🧠 Key Takeaways

* Tree-based ensemble models outperform deep learning on small structured datasets.
* Class imbalance handling is critical in medical AI.
* Recall is the most important metric in screening systems.
* Responsible deployment requires transparency and validation.

## 🛠 Technologies Used

* Python
* Scikit-Learn
* XGBoost
* FastAPI
* Streamlit
* Docker
* Render

## 👨‍⚕️ Author

**Ntimi Mwambasi**
Healthcare AI/ML | Data Science | Clinical Decision Support Systems
