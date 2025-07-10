from django.db import models

# Create your models here.
class userLocation(models.Model) :
    longitude = models.FloatField();
    latitude = models.FloatField();
    # place_type = models.CharField(max_length=100)
    # Added a place_type field to the userLocation model
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude},{self.longitude}"