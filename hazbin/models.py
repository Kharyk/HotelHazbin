from django.db import models

from datetime import datetime, timedelta
from django.db.models import F, ExpressionWrapper, DateTimeField

class Client(models.Model):
    ACCOUNT_TYPES = (
        ('personal', 'Personal'),
        ('business', 'Business'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, default='personal')
    password = models.CharField(max_length=40, null=False)

class Administration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class HotelRooms(models.Model):
    number = models.CharField(max_length=10)
    floor = models.CharField(max_length=3)
    price = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

class Schedule(models.Model):
    day_time = models.DateTimeField()
    end_time = models.DateTimeField(null=False)
    #end_of_work = ExpressionWrapper(F('day_time') + timedelta(hours=8), output_field=DateTimeField())
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE, related_name="schedules")

class Registration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='registrations')
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE, related_name='registrations_administration')
    hotelroom = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, related_name='hotelroom_registrations')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()