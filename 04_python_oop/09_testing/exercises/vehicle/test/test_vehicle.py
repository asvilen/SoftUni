import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.fuel = 100
        self.horse_power = 650
        self.my_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        expected = self.fuel
        actual = self.my_vehicle.fuel
        self.assertEqual(expected, actual)

    def test_drive__when_not_enough_fuel__expect_error(self):
        too_much_kilometers = (self.my_vehicle.fuel / self.my_vehicle.fuel_consumption) + 1
        with self.assertRaises(Exception) as context:
            self.my_vehicle.drive(too_much_kilometers)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_enough_fuel__expect_success(self):
        max_distance = self.my_vehicle.fuel / self.my_vehicle.fuel_consumption
        expected = 0
        self.my_vehicle.drive(max_distance)
        actual = self.my_vehicle.fuel
        self.assertEqual(expected, actual)

    def test_refuel__when_over_capacity__expect_error(self):
        too_much_fuel_to_add = self.my_vehicle.capacity + self.fuel
        with self.assertRaises(Exception) as context:
            self.my_vehicle.refuel(too_much_fuel_to_add)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_not_over_capacity__expect_increase_in_fuel(self):
        distance = 10
        self.my_vehicle.drive(distance)

        fuel_to_refill = distance * self.my_vehicle.fuel_consumption / 2
        expected_fuel = self.my_vehicle.fuel + fuel_to_refill
        self.my_vehicle.refuel(fuel_to_refill)

        self.assertEqual(expected_fuel, self.my_vehicle.fuel)

    def test_str_method(self):
        expected = f"The vehicle has {self.my_vehicle.horse_power} " \
                   f"horse power with {self.my_vehicle.fuel} fuel left and {self.my_vehicle.fuel_consumption} fuel consumption"
        actual = str(self.my_vehicle)
        self.assertEqual(expected, actual)


# if __name__ == "__main__":
#
