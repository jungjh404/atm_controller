import unittest
from atm import ATM
from bank import Bank


class ATMTests(unittest.TestCase):
    def init_bank(self):
        self.bank = Bank({"1111222233334444": {"pin_num": "0000", "account": {"primary": 300000, "saving": 100000000}}})
        self.atm = ATM(self.bank, 1000000)


    def init_card(self):
        self.init_bank()
        self.atm.card_insert("1111222233334444")
        self.atm.pin_check("0000")


    def test_insert_card(self):
        self.init_bank()

        self.assertFalse(self.atm.card_insert("1111"))
        self.assertFalse(self.atm.card_insert("1111a22233334444"))
        self.assertTrue(self.atm.card_insert("1111222233334444"))
        self.assertFalse(self.atm.card_insert("1111222233334444"))
        

    def test_pin_check(self):
        self.init_bank()

        res = self.atm.pin_check("0000")
        self.assertFalse(res[0])
        self.assertEqual(res[1], "Card is not inserted")

        self.atm.card_insert("1111111111111111")
        res = self.atm.pin_check("0000")
        self.assertFalse(res[0])
        self.assertEqual(res[1], "Wrong Card number / PIN number")

        self.atm.card_insert("1111222233334444")
        res = self.atm.pin_check("00000")
        self.assertFalse(res[0])
        self.assertEqual(res[1], "PIN number should be 4 digits long")

        self.atm.card_insert("1111222233334444")
        self.assertTrue(self.atm.pin_check("0000")[0])


    def test_account_select(self):
        self.init_card()
        self.assertFalse(self.atm.select_account("dreaming"))
        self.assertTrue(self.atm.select_account("primary"))


    def test_balance(self):
        self.init_card()
        self.atm.select_account("primary")

        res = self.atm.balance()
        self.assertTrue(res[0])
        self.assertEqual(res[1], 300000)


    def test_deposit(self):
        self.init_card()
        self.atm.select_account("primary")

        res = self.atm.deposit(10000)
        self.assertTrue(res[0])
        self.assertEqual(res[1], 310000)
        self.assertEqual(self.atm.cash_bin, 1010000)


    def test_withdraw(self):
        self.init_card()
        self.atm.select_account("primary")
        res = self.atm.withdraw(10000)
        self.assertTrue(res[0])
        self.assertEqual(res[1], 290000)
        self.assertEqual(self.atm.cash_bin, 990000)

        self.init_card()
        self.atm.select_account("primary")
        res = self.atm.withdraw(310000)
        self.assertFalse(res[0])
        self.assertEqual(res[1], "Not Enough Balance")
        self.assertEqual(self.atm.cash_bin, 1000000)

        self.init_card()
        self.atm.select_account("saving")
        res = self.atm.withdraw(2000000)
        self.assertFalse(res[0])
        self.assertEqual(self.atm.cash_bin, 1000000)


if __name__ == "__main__":
    unittest.main()