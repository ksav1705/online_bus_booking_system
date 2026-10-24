from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_buses, name='search_buses'),
    path('book/<int:schedule_id>/', views.book_seat, name='book_seat'),
    path('ticket/<str:pnr>/', views.view_ticket, name='view_ticket'),
]