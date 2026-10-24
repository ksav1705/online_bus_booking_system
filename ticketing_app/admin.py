from django.contrib import admin
from .models import BusMaster, RouteMaster, ScheduleMaster, TicketBooking

@admin.register(BusMaster)
class BusMasterAdmin(admin.ModelAdmin):
    list_display = ('registration_no', 'bus_type', 'total_capacity')
    search_fields = ('registration_no',)

@admin.register(RouteMaster)
class RouteMasterAdmin(admin.ModelAdmin):
    list_display = ('source_city', 'destination_city', 'distance_km')
    search_fields = ('source_city', 'destination_city')

@admin.register(ScheduleMaster)
class ScheduleMasterAdmin(admin.ModelAdmin):
    list_display = ('bus', 'route', 'departure_time', 'arrival_time', 'base_fare')
    list_filter = ('departure_time', 'route')

@admin.register(TicketBooking)
class TicketBookingAdmin(admin.ModelAdmin):
    list_display = ('pnr_no', 'user', 'schedule', 'payment_status', 'total_amount')
    list_filter = ('payment_status', 'booking_timestamp')
    search_fields = ('pnr_no', 'user__username')