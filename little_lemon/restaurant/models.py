from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000,default='')