"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from apps.room_booking.views import UserRegistrationAPIView, RoomListAPIView, BookRoomAPIView, \
    CancelReservationAPIView, LogoutAPIView, UserLoginAPIView, UserReservationsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/login/', UserLoginAPIView.as_view(), name='api-login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/rooms/', RoomListAPIView.as_view(), name='room-list'),
    path('api/rooms/book/<uuid:room_id>/', BookRoomAPIView.as_view(), name='book-room'),
    path('api/reservations/', UserReservationsAPIView.as_view(), name='reservation-list'),
    path('api/reservations/cancel/<uuid:reservation_id>/', CancelReservationAPIView.as_view(), name='cancel-reservation'),
    path('registration/', TemplateView.as_view(template_name='registration.html'), name='registration'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('rooms/', TemplateView.as_view(template_name='room_list.html'), name='room-list'),
    path('reservations/', login_required(TemplateView.as_view(template_name='reservation_list.html')),
         name='reservation-list'),
]
