from django.db import models


# Create your models here.
class Rooms(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Busy', 'Busy')
    )
    room_number = models.IntegerField(null=False, primary_key=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    guest_name = models.CharField(max_length=25, null=True, blank=True)

