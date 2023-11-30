import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.username = 'Interactive'
        self.level = 5
        self.health = 100
        self.damage = 20
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.me_enemy = Hero(self.username, self.level, self.health, self.damage)
        self.enemy = Hero(self.username + "'s enemy", self.level, self.health, self.damage)

    def test_init(self):
        expected = {'username': 'Interactive', 'level': 5, 'health': 100, 'damage': 10}
        actual = self.hero.__dict__
        self.assertEqual(expected, actual)

    def test_battle__when_enemy_is_same_as_hero__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.me_enemy)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_hero_health_zero_or_less__expect_value_error(self):
        for curr_health in [0, -20]:
            self.hero.health = curr_health
            with self.assertRaises(ValueError) as context:
                self.hero.battle(self.enemy)
            expected = "Your health is lower than or equal to 0. You need to rest"
            self.assertEqual(expected, str(context.exception))

    def test_battle__when_enemy_hero_health_zero_or_less__expect_value_error(self):
        for curr_health in [0, -12]:
            self.enemy.health = curr_health
            with self.assertRaises(ValueError) as context:
                self.hero.battle(self.enemy)
            expected = f"You cannot fight {self.enemy.username}. He needs to rest"
            self.assertEqual(expected, str(context.exception))

    def test_battle__when_two_fighters_go_to_zero_or_below__expect_draw(self):
        expected_health = self.hero.health - self.enemy.damage * self.enemy.level
        expected = 'Draw'
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, self.enemy.health)

    def test_battle__when_enemy_health_goes_zero_or_below__expect_a_win(self):
        self.hero.health = self.enemy.damage * self.enemy.level + 1
        self.enemy.health = self.hero.damage * self.hero.level
        expected = 'You win'
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)
        expected_level = self.level + 1
        expected_health = 1 + 5
        expected_damage = self.damage + 5
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle__when_enemy_above_zero__expect_loss(self):
        self.hero.health = self.enemy.damage * self.enemy.level + 1
        self.enemy.health = self.hero.damage * self.hero.level + 1
        expected = 'You lose'
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)
        expected_level = self.level + 1
        expected_health = 1 + 5
        expected_damage = self.damage + 5
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_str_method(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)
