from project.second_hand_car import SecondHandCar

import unittest


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.model = 'VW Polo'
        self.car_type = 'Hatchback'
        self.mileage = 140000
        self.price = 12000
        self.my_car = SecondHandCar(self.model, self.car_type, self.mileage, self.price)

    def test_init(self):
        self.assertEqual(self.model, self.my_car.model)
        self.assertEqual(self.car_type, self.my_car.car_type)
        self.assertEqual(self.mileage, self.my_car.mileage)
        self.assertEqual(self.price, self.my_car.price)

    def test_price_setter__when_invalid__expect_to_raise_an_error(self):
        expected_error = 'Price should be greater than 1.0!'
        for price in [1, 0]:
            with self.assertRaises(ValueError) as context:
                self.my_car.price = price

            self.assertEqual(expected_error, str(context.exception))

    def test_price_setter__when_valid__expect_price_to_update(self):
        new_price = 10
        self.my_car.price = new_price
        self.assertEqual(new_price, self.my_car.price)

    def test_mileage_setter__when_invalid__expect_to_raise_an_error(self):
        expected_error = 'Please, second-hand cars only! Mileage must be greater than 100!'
        for mileage in [100, 0]:
            with self.assertRaises(ValueError) as context:
                self.my_car.mileage = mileage

            self.assertEqual(expected_error, str(context.exception))

    def test_mileage_setter__when_valid__expect_price_to_update(self):
        new_mileage = 10000
        self.my_car.mileage = new_mileage
        self.assertEqual(new_mileage, self.my_car.mileage)

    def test_set_promotional_price__when_new_price_ge_price__expect_value_error(self):
        error_message = 'You are supposed to decrease the price!'
        for new_price in [self.price, self.price * 2]:
            with self.assertRaises(ValueError) as context:
                self.my_car.set_promotional_price(new_price)
            self.assertEqual(error_message, str(context.exception))

    def test_set_promotional_price__when_new_price_is_valid__expect_success(self):
        new_price = self.price - 1
        expected_result = 'The promotional price has been successfully set.'
        result = self.my_car.set_promotional_price(new_price)
        self.assertEqual(new_price, self.my_car.price)
        self.assertEqual(expected_result, result)

    def test_need_repair__when_too_much_repairs_needed__expect_repair_impossible(self):
        expected_result = 'Repair is impossible!'
        repairs_price = self.price / 2 + 1
        result = self.my_car.need_repair(repairs_price, "")
        self.assertEqual(expected_result, result)

    def test_need_repair__when_can_afford_it__expect_repairs_descr_and_success_message(self):
        expected_result = 'Price has been increased due to repair charges.'
        repairs_price = self.price / 2 - 1
        repair_notes = "Repainted"
        result = self.my_car.need_repair(repairs_price, repair_notes)

        self.assertEqual(expected_result, result)
        self.assertEqual([repair_notes], self.my_car.repairs)

    def test_need_repair__when_can_afford_it_second_time__expect_repairs_list_append_to(self):
        repair_costs = [self.price / 4 - 1, self.price / 4 - 1]
        repair_notes = ["Repainted", "Changed clutch"]
        for idx in range(len(repair_costs)):
            self.my_car.need_repair(repair_costs[idx], repair_notes[idx])
        self.assertEqual(repair_notes, self.my_car.repairs)

    def test_gt__when_diff_type__expect_type_mismatch(self):
        diff_type_car_obj = SecondHandCar(self.model, "Diff Car Type", self.mileage, self.price)
        expected_result = 'Cars cannot be compared. Type mismatch!'
        result = self.my_car > diff_type_car_obj
        self.assertEqual(expected_result, result)

    def test_gt__when_same_type__expect_boolean(self):
        lower_price_car_obj = SecondHandCar(self.model, self.car_type, self.mileage, self.price - 1)
        result = self.my_car > lower_price_car_obj
        self.assertTrue(result)

    def test_str_method(self):
        expected = f"""Model {self.my_car.model} | Type {self.my_car.car_type} | Milage {self.my_car.mileage}km
Current price: {self.my_car.price:.2f} | Number of Repairs: {len(self.my_car.repairs)}"""
        actual = str(self.my_car)
        self.assertEqual(expected, actual)
