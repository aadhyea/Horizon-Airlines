from django.test import TestCase, Client
from django.db.models import Max

# Create your tests here.
from .models import Airport, Flight, Passenger

class FlightTestCase(TestCase):
    def setUp(self):

        #create airports
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        #create flights
        Flight.objects.create(origin=a1, dest=a2, duration=100)
        Flight.objects.create(origin=a1, dest=a1, duration=200)
        Flight.objects.create(origin=a1, dest=a2, duration=-100)

    def test_departures_count(self):
        a= Airport.objects.get(code = "AAA")
        self.assertEqual(a.departures.count(),3)    #'departures' is the related name of 'origin'

    def test_arrival_count(self):
        a= Airport.objects.get(code = "AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1= Airport.objects.get(code = "AAA")
        a2= Airport.objects.get(code = "BBB")
        f = Flight.objects.get(origin=a1, dest=a2, duration=100)        #if origin and dest are different, and duration > 0 
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_dest(self):
        a1= Airport.objects.get(code = "AAA")
        f = Flight.objects.get(origin=a1, dest=a1)      #if origin == dest
        self.assertFalse(f.is_valid_flight())

    def  test_invalid_flight_duration(self):
        a1= Airport.objects.get(code = "AAA")
        a2= Airport.objects.get(code = "BBB")
        f= Flight.objects.get(origin=a1, dest=a2, duration=-100) 
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        c= Client()
        response=c.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)    #a dict is associated with every page that is returned

    def test_valid_flight_page(self):
        # checks if number entered has a valid flight associated with it
        a1=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1, dest=a1)

        c= Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200 )
    
    def test_invalid_flight_page(self):
        #gets the maximum flight ID that is there, and checks if max+1 is invalid
        max_id=Flight.objects.all().aggregate(Max("id"))["id__max"]
        
        c= Client()
        response = c.get(f"/flights/{max_id + 1}")
        self.assertEqual(response.status_code, 404 )




        

         


