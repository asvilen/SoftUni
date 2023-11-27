from worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    name = "Genadi"
    salary = 759
    energy = 59

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_init__when_valid_name_salary_energy__expect_correctly_initialized(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest__when_valid__expect_energy_increment(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_less_than_zero_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_money_increase(self):
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_energy_decrease(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_get_info(self):
        self.money = 0
        expected = f'{self.name} has saved {self.money} money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
