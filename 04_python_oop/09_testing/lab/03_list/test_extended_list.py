from extended_list import IntegerList

import unittest


class TestList(unittest.TestCase):
    integers = [4, 2, 7, 1, 8]

    def setUp(self):
        self.my_list = IntegerList(*self.integers)

    def test_add__when_not_integer__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.add('4')
        self.assertEqual('Element is not Integer', str(context.exception))

    def test_remove_index__when_index_out_of_range__expect_index_error(self):
        out_of_range_index = len(self.my_list.get_data()) + 1
        with self.assertRaises(IndexError) as context:
            self.my_list.remove_index(out_of_range_index)
        self.assertEqual('Index is out of range', str(context.exception))

    def test_init__when_receive_int__expect_to_store_int(self):
        expected = self.integers
        actual = self.my_list.get_data()
        self.assertEqual(expected, actual)

    def test_init__when_non_int__expect_not_to_add_it(self):
        input = [1, "2", 3, 4, "5", 6]
        expected = [1, 3, 4, 6]
        actual = IntegerList(*input).get_data()
        self.assertEqual(expected, actual)

    def test_get__when_index_out_of_range__expect_index_error(self):
        out_of_range_index = len(self.my_list.get_data()) + 1
        with self.assertRaises(IndexError) as context:
            self.my_list.get(out_of_range_index)
        self.assertEqual('Index is out of range', str(context.exception))

    def test_insert__when_index_out_of_range__expect_index_error(self):
        out_of_range_index = len(self.my_list.get_data()) + 1
        with self.assertRaises(IndexError) as context:
            self.my_list.insert(out_of_range_index, 5)
        self.assertEqual('Index is out of range', str(context.exception))

    def test_insert__when_not_int__expect_value_error(self):
        out_of_range_index = len(self.my_list.get_data()) - 1
        with self.assertRaises(ValueError) as context:
            self.my_list.insert(out_of_range_index, "5")
        self.assertEqual('Element is not Integer', str(context.exception))

    def test_get_biggest__when_called__expect_to_return_biggest(self):
        expected = max(self.integers)
        actual = self.my_list.get_biggest()
        self.assertEqual(expected, actual)

    def test_get_index__when_given_el__expect_correct_index(self):
        expected = 0
        actual = self.my_list.get_index(4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
