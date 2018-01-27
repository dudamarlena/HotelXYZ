
from django.views.generic import ListView
from hotel.models import Rooms


# Create your views here.
class RoomsView(ListView):
    queryset = Rooms.objects.all()
    template_name = 'hotel/rooms.html'
