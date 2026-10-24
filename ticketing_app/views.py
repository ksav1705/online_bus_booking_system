from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ScheduleMaster, TicketBooking
from .services import process_seat_booking
from datetime import datetime

def home(request):
    """Renders the landing page with the search form."""
    return render(request, 'search_home.html')

def search_buses(request):
    """Handles the search logic."""
    if request.method == 'POST':
        source = request.POST.get('source_city')
        destination = request.POST.get('destination_city')
        travel_date_str = request.POST.get('travel_date')

        try:
            travel_date = datetime.strptime(travel_date_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'search_error.html', {'error': 'Invalid Date Format'})

        available_schedules = ScheduleMaster.objects.filter(
            route__source_city__icontains=source,
            route__destination_city__icontains=destination,
            departure_time__date=travel_date
        ).select_related('bus', 'route').order_by('departure_time')

        context = {
            'schedules': available_schedules,
            'search_params': {'source': source, 'dest': destination, 'date': travel_date_str}
        }
        return render(request, 'bus_list.html', context)
        
    return redirect('home')

@login_required(login_url='/login/')
def book_seat(request, schedule_id):
    """Handles the seat booking submission."""
    schedule = get_object_or_404(ScheduleMaster, pk=schedule_id)
    
    if request.method == 'POST':
        # Expecting a comma-separated string of seats from a hidden form field
        seats_raw = request.POST.get('selected_seats') 
        selected_seats = [s.strip() for s in seats_raw.split(',') if s.strip()]
        
        # Simple fare calculation (Number of seats * Base Fare)
        total_fare = len(selected_seats) * schedule.base_fare
        
        try:
            pnr = process_seat_booking(request.user, schedule.schedule_id, selected_seats, total_fare)
            # In a real app, redirect to payment gateway here. 
            # We will redirect to the ticket view for the project scope.
            return redirect('view_ticket', pnr=pnr)
        except Exception as e:
             return render(request, 'checkout.html', {'schedule': schedule, 'error': str(e)})

    return render(request, 'checkout.html', {'schedule': schedule})

@login_required
def view_ticket(request, pnr):
    """Displays the final E-Ticket."""
    ticket = get_object_or_404(TicketBooking, pnr_no=pnr, user=request.user)
    return render(request, 'ticket_view.html', {'ticket': ticket})