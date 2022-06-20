import unittest
from atm import ATM
from bank import Bank


class ATMTests(unittest.TestCase):
    def init_card(self):
        self.bank = Bank({"1111222233334444": {"pin_num": "0000", "account": {"primary": 300000, "saving": 100000000}}})
        self.atm = ATM(self.bank, 1000000)
        self.atm.card_init("1111222233334444", "0000")


    def test_card_init(self):
        self.bank = Bank({"1111222233334444": {"pin_num": "0000", "account": {"primary": 300000, "saving": 100000000}}})
        self.atm = ATM(self.bank, 1000000)

        self.assertFalse(self.atm.card_init("1111111111111111", "0000"))
        self.assertFalse(self.atm.card_init("1111222233334444", "1111"))
        self.assertTrue(self.atm.card_init("1111222233334444", "0000"))
        
    
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

        self.init_card()
        self.atm.select_account("saving")

        res = self.atm.withdraw(2000000)
        self.assertFalse(res[0])
        self.assertEqual(res[1], "Not Enough Cash Bin")


if __name__ == "__main__":
    unittest.main()