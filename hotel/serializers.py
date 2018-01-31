from rest_framework import serializers
from hotel.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number', 'guest_name')