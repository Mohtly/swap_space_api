from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Matches(models.Model):
    matches_id = models.AutoField(primary_key=True)
    item_id_1 = models.IntegerField()
    item_id_2 = models.IntegerField()
    date_time_created = models.DateTimeField(auto_now_add=True)