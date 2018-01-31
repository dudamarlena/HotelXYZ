from django import forms
from hotel.models import Room


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number']
