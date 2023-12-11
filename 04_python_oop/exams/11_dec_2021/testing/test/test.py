import unittest

from project.team import Team


class TestTeam(unittest.TestCase):
    _TEAM_NAME_ERROR_MSG = "Team Name can contain only letters!"

    def setUp(self):
        self.name = 'Malmo'
        self.members = {
            'Zlatan Ibrahimovic': 16,
            'Toni Montana': 16,
            'Kiki': 13,
            'Alice': 15,
        }
        self.team = Team(self.name)
        self.team.add_member(**self.members)

    def test_init(self):
        self.assertEqual(self.name, self.team.name)
        self.assertDictEqual(self.members, self.team.members)

    def test_name_property__when_name_has_letters_only__expect_to_set_successfully(self):
        new_name = 'Ajax'
        self.team.name = new_name
        self.assertEqual(new_name, self.team.name)

    def test_name_property__when_name_has_non_alphabetic_chars__expect_to_raise_exception(self):
        new_name = 'Ajax 1878'
        with self.assertRaises(ValueError) as context:
            self.team.name = new_name
        self.assertEqual(self._TEAM_NAME_ERROR_MSG, str(context.exception))

    def test_add_member__when_one_member_only__expect_to_add_it_successfully(self):
        new_member = {'Snejder': 19}
        expected_message = f"Successfully added: {', '.join(new_member)}"
        result = self.team.add_member(**new_member)
        self.assertTrue(name in self.team.members.keys() for name in new_member)
        self.assertEqual(expected_message, result)

    def test_add_member__when_multiple_new_members__expect_to_add_all(self):
        new_members = {
            'der Vaart': 17,
            'Blind': 22,
        }
        expected_message = f"Successfully added: {', '.join(new_members)}"
        result = self.team.add_member(**new_members)
        self.assertTrue(name in self.team.members.keys() for name in new_members)
        self.assertEqual(expected_message, result)

    def test_add_member__when_name_exists__expect_empty_result_list(self):
        new_members = {
            'Zlatan Ibrahimovic': 16,
            'Toni Montana': 16,
        }
        expected_message = f"Successfully added: {', '.join([])}"
        result = self.team.add_member(**new_members)
        self.assertTrue(name in self.team.members.keys() for name in new_members)
        self.assertEqual(expected_message, result)

    def test_remove_member__when_name_exists__expect_to_remove_the_name(self):
        name = 'Toni Montana'
        expected_msg = f"Member {name} removed"
        result = self.team.remove_member(name)
        self.assertEqual(expected_msg, result)

    def test_remove_member__when_name_does_not_exists__expect_to_remove_no_one(self):
        name = 'Van Basten'
        expected_msg = f"Member with name {name} does not exist"
        result = self.team.remove_member(name)
        self.assertEqual(expected_msg, result)

    def test_gt__when_has_more_members__expect_true(self):
        other_team = Team('Juventus')
        other_team.add_member(**{'Luca Tonu': 17})
        self.assertTrue(self.team > other_team)

    def test_gt__when_has_equal_number_of_members__expect_false(self):
        other_team = Team('Juventus')
        members = {
            'Zlatan Ibrahimovic': 16,
            'Toni Montana': 16,
            'Kiki': 13,
            'Alice': 15,
        }
        other_team.add_member(**members)
        self.assertFalse(self.team > other_team)

    def test_gt__when_has_less_members__expect_false(self):
        other_team = Team('Juventus')
        members = {
            'Zlatan Ibrahimovic': 16,
            'Toni Montana': 16,
            'Kiki': 13,
            'Alice': 15,
            'Luca Toni': 17,
        }
        other_team.add_member(**members)
        self.assertFalse(self.team > other_team)

    def test_len(self):
        self.assertEqual(4, len(self.team))

    def test_add__when_two_different_teams__expect_new_team_with_their_names_and_members(self):
        other_team = Team('Juventus')
        members = {
            'Filipo Indzhagi': 16,
            'Pirlo': 16,
            'Kiki': 13,
        }
        other_team.add_member(**members)
        resulting_team = self.team + other_team

        expected_name = f"{self.team.name }{other_team.name}"
        actual_name = resulting_team.name
        self.assertEqual(expected_name, actual_name)
        self.team.add_member(**members)
        expected_members = self.team.members
        actual_members = resulting_team.members
        self.assertDictEqual(expected_members, actual_members)

    def test_add__when_the_same_team__expect_new_team_same_members(self):
        resulting_team = self.team + self.team
        expected_name = f"{self.team.name }{self.team.name}"
        actual_name = resulting_team.name
        self.assertEqual(expected_name, actual_name)
        expected_members = self.team.members
        actual_members = resulting_team.members
        self.assertDictEqual(expected_members, actual_members)

    def test_str_method(self):
        result = [f"Team name: {self.team.name}"]
        members = list(sorted(self.team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected = "\n".join(result)
        actual = str(self.team)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()