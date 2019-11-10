from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    # Right now each item can only have one photo
    photo = models.TextField()
    # This should be updated to set the value of an item between some range for searching
    value_low = models.IntegerField()
    value_high = models.IntegerField()
    user_id = models.IntegerField()
    description = models.TextField()
    traded = models.BooleanField()
    date_time_created = models.DateTimeField(auto_now_add=True)