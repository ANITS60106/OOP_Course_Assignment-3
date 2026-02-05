import unittest
from account import PersonalAccount


class TestPersonalAccount(unittest.TestCase):
    def test_deposit_increases_balance(self):
        acc = PersonalAccount(1, "Ramazan")
        acc.deposit(100)
        self.assertEqual(acc.get_balance(), 100.0)

    def test_withdraw_decreases_balance(self):
        acc = PersonalAccount(2, "Aidai")
        acc.deposit(200)
        acc.withdraw(50)
        self.assertEqual(acc.get_balance(), 150.0)

    def test_withdraw_more_than_balance_raises(self):
        acc = PersonalAccount(3, "Chyngyz")
        acc.deposit(30)
        with self.assertRaises(ValueError):
            acc.withdraw(100)

    def test_operator_add_calls_deposit(self):
        acc = PersonalAccount(4, "Jail")
        acc + 25
        self.assertEqual(acc.get_balance(), 25.0)

    def test_operator_sub_calls_withdraw(self):
        acc = PersonalAccount(5, "Emir")
        acc.deposit(40)
        acc - 10
        self.assertEqual(acc.get_balance(), 30.0)


if __name__ == "main":
    unittest.main()