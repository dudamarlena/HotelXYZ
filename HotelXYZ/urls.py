"""HotelXYZ URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
from hotel.views import RoomView, AddRoomView, reservation

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', RoomView.as_view(), name="room"),
    url(r'^add/', AddRoomView.as_view(), name="add room"),
    url(r'^reservation/', reservation, name="reservation"),
]
