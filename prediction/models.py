from django.db import models
from django.contrib.auth.models import User

class PredictionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='Female')
    pregnancies = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    age = models.IntegerField()
    result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.result} - {self.created_at}"
