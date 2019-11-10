from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    # rating = models.FloatField(MaxValueValidator(100.00), MinValueValidator(0.00))
    # number_of_ratings
    date_time_created = models.DateTimeField(auto_now_add=True)