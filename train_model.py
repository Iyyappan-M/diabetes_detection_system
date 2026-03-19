import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_and_save_model():
    print("Downloading dataset...")
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    columns = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
        "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
    ]
    df = pd.read_csv(url, header=None, names=columns)

    # Note: Pima dataset is all female. Adding Gender=0 (Female).
    # Model will be trained with 7 features in this specific order:
    # [Pregnancies, Glucose, BloodPressure, Insulin, BMI, Age, Gender]
    df['Gender'] = 0
    
    features = ["Pregnancies", "Glucose", "BloodPressure", "Insulin", "BMI", "Age", "Gender"]
    X = df[features]
    y = df["Outcome"]

    print(f"Training on features: {features}")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save model and scaler
    model_dir = 'prediction'
    joblib.dump(model, os.path.join(model_dir, 'ml_model.pkl'))
    joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))
    print("Model and scaler updated successfully with 7 features.")

if __name__ == "__main__":
    train_and_save_model()
