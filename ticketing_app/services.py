from django.db import transaction
from .models import ScheduleMaster, TicketBooking
import uuid

def process_seat_booking(user, schedule_id, selected_seats, total_amount):
    with transaction.atomic():
        try:
            schedule = ScheduleMaster.objects.select_for_update().get(schedule_id=schedule_id)
            
            existing_bookings = TicketBooking.objects.filter(
                schedule=schedule, 
                payment_status__in=['SUCCESS', 'PENDING']
            )
            
            booked_seat_list = []
            for booking in existing_bookings:
                booked_seat_list.extend(booking.seat_numbers.split(','))
                
            for seat in selected_seats:
                if seat.strip() in booked_seat_list:
                    raise Exception(f"Seat {seat} has already been taken. Please select another.")
            
            unique_pnr = f"PNR-{uuid.uuid4().hex[:8].upper()}"
            
            new_ticket = TicketBooking.objects.create(
                pnr_no=unique_pnr,
                user=user,
                schedule=schedule,
                seat_numbers=",".join(selected_seats),
                total_amount=total_amount,
                payment_status='SUCCESS' # Marked success for testing purposes
            )
            
            return new_ticket.pnr_no
            
        except ScheduleMaster.DoesNotExist:
            raise Exception("Invalid Schedule Selected.")