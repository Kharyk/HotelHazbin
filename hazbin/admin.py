from django.contrib import admin

from .models import Client, Administration, HotelRooms, Registration, Schedule

admin.site.register(Client)
admin.site.register(Administration)
admin.site.register(HotelRooms)
admin.site.register(Registration)
admin.site.register(Schedule)


# Register your models here.
