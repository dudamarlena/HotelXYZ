from rest_framework import serializers
from hotel.models import Rooms


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('room_number', 'guest_name')