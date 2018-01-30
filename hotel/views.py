from django.views.generic import ListView, CreateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hotel.forms import AddRoomForm
from hotel.models import Rooms
from hotel.serializers import RoomSerializer


class RoomsView(ListView):
    model = Rooms
    template_name = 'hotel/rooms.html'


class AddRoomView(CreateView):
    form_class = AddRoomForm
    template_name = 'hotel/add_room.html'
    success_url = "/home/"


@api_view(['GET', 'POST'])
def reservation(request, format=None):
    if request.method == 'GET':
        rooms = Rooms.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            serializer = RoomSerializer(data=request.data)
            room_number = serializer.initial_data.get("room_number")
            guest_name = serializer.initial_data.get("guest_name")
            room = Rooms.objects.get(room_number=room_number)
        except Rooms.DoesNotExist:
            return Response("This room has not exists", status=status.HTTP_404_NOT_FOUND)

        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            room_number = serializer.data.get("room_number")
            room = Rooms.objects.get(room_number=room_number)
            if room.status == "Available":
                room.status = "Busy"
                room.guest_name = guest_name
                room.save()
            else:
                return Response("This room is busy", status=status.HTTP_400_BAD_REQUEST)
            return Response("Added a new reservation", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
