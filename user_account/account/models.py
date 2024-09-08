from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile= models.CharField(max_length=15)
    license = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    did = models.CharField(max_length=10, unique=True)
    password= models.CharField(max_length=100)
    photo = models.ImageField(upload_to='driver_photos/')

    def __str__(self):
        return self.name

#trip

class Trip(models.Model):
    trip_from = models.CharField(max_length=255)
    trip_to = models.CharField(max_length=255)
    meter_reading_before = models.CharField(max_length=50)
    meter_reading_after = models.CharField(max_length=50)
    filled_fuel = models.DecimalField(max_digits=10, decimal_places=2)
    credit_point = models.CharField(max_length=50)
    trip_mode = models.CharField(max_length=20, choices=[('Load', 'Load'), ('Empty', 'Empty'), ('Others', 'Others')])
    invoice_document = models.FileField(upload_to='documents/')
    note = models.TextField()
    status_update = models.CharField(max_length=50, choices=[
        ('start', 'Trip Start From Godown'), ('reachD', 'Reach Destination'),
        ('pick', 'Pick Up (Product)'), ('starts', 'Pick Up And Start Trip'),
        ('reachG', 'Reach Godown'), ('problem', 'Problem'), ('ongoing', 'Trip Ongoing')
    ])
    location = models.CharField(max_length=255)
    report_date = models.DateField()
    report_time = models.TimeField()
    trip_start_date = models.DateField()
    trip_end_date = models.DateField()
    category_name = models.CharField(max_length=255)
    truck_weight_before = models.FileField(upload_to='weights/')
    truck_weight_after_load = models.FileField(upload_to='weights/')
    truck_weight_after_godown = models.FileField(upload_to='weights/')

    def __str__(self):
        return f"{self.trip_from} to {self.trip_to}"
