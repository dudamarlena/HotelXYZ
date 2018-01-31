from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Room
from .forms import AddRoomForm
from .serializers import RoomSerializer

import json


class RoomsModelTest(TestCase):
    def test_int_representation(self):
        room = Room(room_number=1)
        self.assertEqual(1, room.room_number)

    def test_string_representation(self):
        guest = Room(guest_name="Nowak")
        self.assertEqual("Nowak", guest.guest_name)

    def test_none_data(self):
        Room(guest_name=None)
        self.assertRaises(ValidationError)

    def test_double_data(self):
        Room.objects.create(room_number=1)
        self.assertRaises(IntegrityError)


class AddRoomFormTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_number=1)

    def test_valid_data(self):
        form = AddRoomForm({"room_number": 1},
                           instance=self.room)

        self.assertTrue(form.is_valid())
        rooms = form.save()
        self.assertEqual(rooms.room_number, 1)

    def test_blank_data(self):
        form = AddRoomForm({}, instance=self.room)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'room_number': ['This field is required.']
        })


class RoomSerializerTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_number=1, guest_name="Nowak")
        self.data = {"room_number": 1, "guest_name": "Nowak"}

    def test_client_get(self):
        response = self.client.get('/reservation/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [self.data])

    def test_client_post(self):
        request = self.client.post('/reservation/', self.data, format='json')
        self.assertEqual(request.status_code, 201)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().room_number, 1)
        self.assertEqual(Room.objects.get().guest_name, "Nowak")

    def test_serializer(self):
        serializer = RoomSerializer(self.room, data=self.data)
        self.assertTrue(serializer.is_valid())
