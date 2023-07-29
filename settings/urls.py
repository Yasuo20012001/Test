from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from apps.room_booking.views import (BookRoomAPIView, CancelReservationAPIView,
                                     LogoutAPIView, RoomListAPIView,
                                     UserLoginAPIView, UserRegistrationAPIView,
                                     UserReservationsAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
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
