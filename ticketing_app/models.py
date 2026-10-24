from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BusMaster(models.Model):
    bus_id = models.AutoField(primary_key=True)
    registration_no = models.CharField(max_length=20, unique=True)
    BUS_TYPES = (
        ('AC_SLEEPER', 'AC Sleeper'),
        ('NON_AC', 'Non-AC Seater'),
        ('VOLVO', 'Volvo Semi-Sleeper')
    )
    bus_type = models.CharField(max_length=15, choices=BUS_TYPES)
    total_capacity = models.IntegerField()
    
    def __str__(self):
        return f"{self.registration_no} ({self.get_bus_type_display()})"

class RouteMaster(models.Model):
    route_id = models.AutoField(primary_key=True)
    source_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.source_city} to {self.destination_city}"

class ScheduleMaster(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(BusMaster, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteMaster, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_fare = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.route} - {self.departure_time.strftime('%Y-%m-%d %H:%M')}"

class TicketBooking(models.Model):
    pnr_no = models.CharField(max_length=15, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduleMaster, on_delete=models.CASCADE)
    seat_numbers = models.CharField(max_length=255) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    booking_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pnr_no