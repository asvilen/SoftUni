import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.name = 'Mikki'
        self.type = 'Monkey'
        self.sound = 'Suuuututu'
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_init(self):
        self.mammal = Mammal('Mikki', 'Monkey', 'Suuuututu')
        expected = {'name': 'Mikki', 'type': 'Monkey', 'sound': 'Suuuututu', '_Mammal__kingdom': 'animals'}
        actual = self.mammal.__dict__
        self.assertEqual(expected, actual)

    def test_make_sound(self):
        expected = f"{self.name} makes {self.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info(self):
        expected = f"{self.name} is of type {self.type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)