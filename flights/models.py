from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"
    

class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    dest=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}:{self.origin} to {self.dest}"
    
    def is_valid_flight(self):
        return self.origin != self.dest and self.duration >0
        #if logic is wrong, then tests will return AssetionError 
    

class Passenger(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")      #many passengers can have many different flights

    def __str__(self) -> str:
        return f"{self.first} {self.last}"
    

