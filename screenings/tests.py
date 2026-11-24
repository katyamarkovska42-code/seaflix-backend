from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from screenings.models import Auditorium


class AuditoriumModelTest(TestCase):
    def test_str_shows_name_and_building(self):
        auditorium = Auditorium.objects.create(
            name='1-225',
            building='Корпус 1',
            capacity=40,
        )
        self.assertEqual(str(auditorium), '1-225 (Корпус 1)')

    def test_is_active_by_default(self):
        auditorium = Auditorium.objects.create(
            name='1-225',
            building='Корпус 1',
            capacity=40,
        )
        self.assertTrue(auditorium.is_active)

    def test_capacity_must_be_positive(self):
        auditorium = Auditorium(
            name='1-225',
            building='Корпус 1',
            capacity=0,
        )
        with self.assertRaises(ValidationError):
            auditorium.full_clean()

    def test_same_name_in_same_building_is_not_allowed(self):
        Auditorium.objects.create(
            name='1-225',
            building='Корпус 1',
            capacity=40,
        )
        with self.assertRaises(IntegrityError):
            Auditorium.objects.create(
                name='1-225',
                building='Корпус 1',
                capacity=30,
            )

    def test_same_name_in_different_building_is_allowed(self):
        Auditorium.objects.create(
            name='225',
            building='Корпус 1',
            capacity=40,
        )
        other = Auditorium.objects.create(
            name='225',
            building='Корпус 3',
            capacity=30,
        )
        self.assertEqual(other.building, 'Корпус 3')
