import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.PositiveIntegerField(blank=False, null=False)
    capacity = models.PositiveIntegerField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=8, decimal_places=2,
        blank=False, null=False
    )

    objects = models.Manager()


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    check_in = models.DateField(auto_now=False)
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user.username} - {self.room.room}"
