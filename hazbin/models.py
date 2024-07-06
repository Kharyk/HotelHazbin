from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()



class Administration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class HotelRooms(models.Model):
    numder = models.CharField(max_length=10)
    floor = models.CharField(max_length=3)
    price = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    

class Schedule(models.Model):
    day_time = models.DateTimeField()
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE, related_name="schedules")
    
class Registration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='registrations')
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE, related_name='registrations_administration')
    hotelroom = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, related_name='hotelroom_registrations')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    


# Create your models here.

