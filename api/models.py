from django.db import models

class Geocode(models.Model):
  search_term = models.CharField(max_length = 200, primary_key = True)
  address_string = models.CharField(max_length = 200, null=True)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)
  
  def __str__(self):
    return self.address_string