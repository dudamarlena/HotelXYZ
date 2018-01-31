from django.db import models


class Room(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Busy', 'Busy')
    )
    room_number = models.IntegerField(null=False, primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')
    guest_name = models.CharField(max_length=25, null=True, blank=True, default=None)

    class Meta:
        ordering = ['room_number']
