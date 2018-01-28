from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from hotel.models import Rooms


# Create your views here.
# class RoomsView(ListView):
#     queryset = Rooms.objects.all()
#     template_name = 'hotel/rooms.html'

def rooms_view(request):
    print(request)
    if request.method == 'POST':
        obj = Rooms.objects.create(
            room_number=request.POST.get("room_number"),
            status="Available",
            guest_name=None)
    template_name = 'hotel/rooms.html'
    queryset = Rooms.objects.all()
    context = {"rooms_list": queryset}
    return render(request, template_name, context)

#
