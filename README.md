# Diabetes Detection System - Setup Instructions

This project is a Django web application that uses Machine Learning to predict diabetes based on health metrics.

## Prerequisites
- Python 3.10 or higher
- VS Code (Recommended)

## Setup and Run Instructions

### 1. Open the project in VS Code
Open the folder `c:\Users\Asus\game\diabetes_detection_system` in VS Code.

### 2. Set up the Environment
The project already comes with a virtual environment (`venv`) and pre-trained model.
Ensure you have the required packages:
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Setup (Already done)
Migrations have been applied and a superuser created.
- **Admin Username:** `admin`
- **Admin Password:** `admin`

### 4. Run the Application
Start the Django development server:
```powershell
python manage.py runserver
```

### 5. Access the Web App
Open your browser and go to:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- `users/`: Handles registration, login, and home page.
- `prediction/`: Handles ML logic, data input, and results.
- `templates/`: HTML files with Bootstrap styling.
- `static/`: CSS and JS files.
- `ml_models/`: Contains the pre-trained `RandomForest` model and `StandardScaler`.
- `train_model.py`: Script used to train the model on the Pima Indians Dataset.

## Features
- **Machine Learning:** Random Forest model trained on clinical data.
- **User System:** Secure registration and login.
- **Admin Portal:** Manage users and view all prediction history.
- **Records:** Every prediction is saved to the SQLite database.
- **Responsive UI:** Modern design using Bootstrap and custom CSS.
