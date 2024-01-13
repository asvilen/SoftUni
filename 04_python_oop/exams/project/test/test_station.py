import unittest

from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    _INVALID_NAME_MSG = "Name should be more than 3 symbols!"

    def setUp(self):
        self.name = 'Gara Yug'
        self.station = RailwayStation(self.name)

    def test_init(self):
        self.name = 'Gara Yug'
        self.station = RailwayStation(self.name)
        self.assertEqual(self.name, self.station.name)
        self.assertTrue(deque([]) == self.station.arrival_trains)
        self.assertTrue(deque([]) == self.station.departure_trains)

    def test_name__when_less_than_3_chars__expect_to_raise(self):
        name = 'Ga'
        with self.assertRaises(ValueError) as context:
            RailwayStation(name)
        self.assertEqual(self._INVALID_NAME_MSG, str(context.exception))

    def test_name__when_with_3_chars__expect_to_raise(self):
        name = 'Gar'
        with self.assertRaises(ValueError) as context:
            RailwayStation(name)
        self.assertEqual(self._INVALID_NAME_MSG, str(context.exception))

    def test_new_arrival_on_board__append_input(self):
        train_info = 'Train N.1'
        expected = deque([train_info])
        self.station.new_arrival_on_board(train_info)
        actual = self.station.arrival_trains

        self.assertEqual(expected, actual)

    def test_train_has_arrived__when_no_trains_in_deque__expect_index_error(self):
        train = 'Train N.2'
        # self.station.new_arrival_on_board(train)

        # expected = deque([train_info])
        with self.assertRaises(IndexError):
            self.station.train_has_arrived(train)

    def test_train_has_arrived__when_not_input_s_turn__expect_wait_message(self):
        train = 'Train N.2'
        self.station.new_arrival_on_board(train)
        train_2 = 'Train N.3'
        expected = f"There are other trains to arrive before {train_2}."
        actual = self.station.train_has_arrived(train_2)
        self.assertEqual(expected, actual)

    def test_train_has_arrived__when_input_s_turn__expect_append_to_departures_and_success_msg(self):
        train = 'Train N.2'
        self.station.new_arrival_on_board(train)
        expected = f"{train} is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived(train)
        self.assertEqual(expected, actual)
        self.assertEqual(deque([train]), self.station.departure_trains)

    def test_train_has_left__when_no_departure_trains__expect_false(self):
        train = 'Train N.5'
        result = self.station.train_has_left(train)
        self.assertFalse(result)

    def test_train_has_left__when_input_train_s_turn__expect_to_remove_from_dep_deque_and_true(self):
        train = 'Train N.5'
        self.station.departure_trains.append(train)
        result = self.station.train_has_left(train)
        self.assertEqual(deque([]), self.station.departure_trains)
        self.assertTrue(result)

    def test_train_has_left__when_not_input_train_s_turn__expect_false(self):
        train_1 = 'Train N.7'
        train_2 = 'Train N.8'
        self.station.departure_trains.append(train_1)
        self.station.departure_trains.append(train_2)
        result = self.station.train_has_left(train_2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()