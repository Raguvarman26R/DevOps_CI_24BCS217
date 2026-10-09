import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.app import (
    book_appointment,
    view_appointments,
    cancel_appointment,
    appointments
)


class TestHospitalAppointment(unittest.TestCase):

    def setUp(self):
        appointments.clear()

    def test_book_appointment(self):
        result = book_appointment(
            "Arun", "Dr. Kumar", "2026-10-15", "10:00 AM"
        )
        self.assertEqual(
            result, "Appointment booked successfully"
        )

    def test_missing_patient(self):
        result = book_appointment(
            "", "Dr. Kumar", "2026-10-15", "10:00 AM"
        )
        self.assertEqual(result, "All fields are required")

    def test_view_appointments(self):
        book_appointment(
            "Arun", "Dr. Kumar", "2026-10-15", "10:00 AM"
        )
        self.assertEqual(len(view_appointments()), 1)

    def test_cancel_appointment(self):
        book_appointment(
            "Arun", "Dr. Kumar", "2026-10-15", "10:00 AM"
        )
        result = cancel_appointment("Arun")
        self.assertEqual(
            result, "Appointment cancelled successfully"
        )


if __name__ == "__main__":
    unittest.main()