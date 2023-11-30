from car_manager import Car

import unittest


class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.make = 'Toyota'
        self.model = 'Supra'
        self.fuel_consumption = 50
        self.fuel_capacity = 70
        self.fuel_amount = 0
        self.car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_make__when_null_empty__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car_manager.make = ''
        self.assertEqual('Make cannot be null or empty!', str(context.exception))