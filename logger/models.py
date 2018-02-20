from django.db import models
from django.utils import timezone


class WaterLog(models.Model):
  distance = models.CharField(max_length=400)
  rTCtemp = models.CharField(max_length=400)
  watertemp = models.CharField(max_length=400)
  airttemp = models.CharField(max_length=400)
  created_date = models.DateTimeField(
            default=timezone.now)
  def publish(self, distance, rTCtemp, watertemp, airtemp):
    self.created_date = timezone.now()
    self.distance = distance
    self.rTCtemp = rTCtemp
    self.watertemp = watertemp
    self.airtemp = airtemp
    self.save()
  def __str__():
    return str(self.created_date)
# Create your models here.
