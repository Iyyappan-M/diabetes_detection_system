from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import PredictionRecord
from .ml_logic import make_prediction
import logging

logger = logging.getLogger(__name__)

@login_required
def predict_view(request):
    if request.method == 'POST':
        try:
            # 1. Capture Gender
            gender_str = request.POST.get('gender')
            if not gender_str:
                return render(request, 'predict.html', {'error': 'Please select a Gender.'})
            
            # Male = 1, Female = 0
            gender_val = 1.0 if gender_str == 'Male' else 0.0
            
            # 2. Extract and validate all fields individually for better error reporting
            try:
                # Logic for conditional pregnancies
                if gender_str == 'Male':
                    pregnancies = 0.0
                else:
                    pregnancies_raw = request.POST.get('pregnancies')
                    pregnancies = float(pregnancies_raw) if pregnancies_raw and pregnancies_raw.strip() != "" else 0.0

                glucose = float(request.POST.get('glucose', 0))
                blood_pressure = float(request.POST.get('blood_pressure', 0))
                insulin = float(request.POST.get('insulin', 0))
                bmi = float(request.POST.get('bmi', 0))
                age = float(request.POST.get('age', 0))
            except (ValueError, TypeError) as e:
                logger.error(f"Data conversion error: {e}")
                return render(request, 'predict.html', {'error': 'One or more fields contain invalid numbers. Please check your inputs.'})

            # 3. Create input array in exact order: 
            # [Pregnancies, Glucose, BloodPressure, Insulin, BMI, Age, Gender]
            data = [
                pregnancies,
                glucose,
                blood_pressure,
                insulin,
                bmi,
                age,
                gender_val
            ]
            
            # 4. Run ML Model
            result = make_prediction(data)
            
            # 5. Save to database
            record = PredictionRecord.objects.create(
                user=request.user,
                gender=gender_str,
                pregnancies=int(pregnancies),
                glucose=glucose,
                blood_pressure=blood_pressure,
                insulin=insulin,
                bmi=bmi,
                age=int(age),
                result=result
            )
            
            # 6. Show result
            request.session['prediction_id'] = record.id
            return redirect('result')
            
        except Exception as e:
            logger.exception("Unexpected error in predict_view")
            return render(request, 'predict.html', {'error': f'An unexpected error occurred: {str(e)}'})
            
    return render(request, 'predict.html')

@login_required
def result_view(request):
    prediction_id = request.session.get('prediction_id')
    if not prediction_id:
        return redirect('predict')
    
    try:
        record = PredictionRecord.objects.get(id=prediction_id)
        return render(request, 'result.html', {'record': record})
    except PredictionRecord.DoesNotExist:
        return redirect('predict')

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    users = User.objects.all()
    predictions = PredictionRecord.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {
        'users': users,
        'predictions': predictions
    })

@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if not user.is_staff:
        user.delete()
    return redirect('admin_dashboard')
