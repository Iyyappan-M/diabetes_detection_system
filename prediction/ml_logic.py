import joblib
import os
import numpy as np
from django.conf import settings

# Paths to model and scaler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'prediction', 'ml_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'prediction', 'scaler.pkl')

# Load once when module starts
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def make_prediction(data):
    """
    data: list of 7 features [Pregnancies, Glucose, BloodPressure, Insulin, BMI, Age, Gender]
    """
    features = np.array(data).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
