from cat import Cat

import unittest


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_eat__when_fed__expect_size_increase(self):
        expected = self.cat.size + 1
        self.cat.eat()
        actual = self.cat.size
        self.assertEqual(expected, actual)

    def test_eat__when_eat__expect_fed(self):
        self.cat.eat()
        actual = self.cat.fed
        self.assertTrue(actual)

    def test_eat__when_fed__expect_cannot_eat(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep__when_hungry__expect_cannot_sleep(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_sleep__when_slept__expect_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleep()
        actual = self.cat.sleepy
        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()
