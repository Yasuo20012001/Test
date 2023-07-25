from django.contrib import admin

from apps.room_booking.models import Reservation, Room


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'price', 'capacity')
    search_fields = ('number',)


# @admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out')
    list_filter = ('check_in', 'check_out')
    search_fields = ('room__room', 'user__username')


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
