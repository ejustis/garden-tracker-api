from django.db import models
import datetime

# Create your models here.
class SunExposure(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    garden_id = models.CharField(max_length=100,blank=False)
    lux_value = models.IntegerField(blank=False)

    class Meta:
        db_table = "sunexposures"