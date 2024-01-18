from django.contrib import admin

# Register your models here.
from .models import Flight,Airport,Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","dest","duration")  #when displaying flights, display in this format
 
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger,PassengerAdmin )