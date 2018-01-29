# HotelXYZ URL Configuration

from django.conf.urls import url
from django.contrib import admin
from hotel.views import RoomsView, AddRoomView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', RoomsView.as_view(), name="rooms"),
    url(r'^add/', AddRoomView.as_view(), name="add room"),

]
