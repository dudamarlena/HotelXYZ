from django import forms
from hotel.models import Rooms


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['room_number']
