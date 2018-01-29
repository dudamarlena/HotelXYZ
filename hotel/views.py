from django.views.generic import ListView, CreateView
from hotel.forms import AddRoomForm
from hotel.models import Rooms


class RoomsView(ListView):
    model = Rooms
    template_name = 'hotel/rooms.html'


class AddRoomView(CreateView):
    form_class = AddRoomForm
    template_name = 'hotel/add_room.html'
    success_url = "/home/"
