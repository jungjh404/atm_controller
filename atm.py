from bank import Bank


class ATM:
    def __init__(self, bank, cash_bin):
        self.bank = bank
        self.cash_bin = cash_bin
        self.user_card = None


    def card_init(self, card_num, pin_num):
        res = self.bank.check_pin(card_num, pin_num)
        if not res:
            return False
        
        self.user_card = card_num
        return True
    





if __name__ == "__main__":
    bank = Bank({"1111222233334444": {"pin_num": "0000", "account": {"primary": 300000, "saving": 100000000}}})
    atm = ATM(bank, 1000000)
    
    # Check Card Init
    atm.card_init("1111111111111111", "0000")
    atm.card_init("1111222233334444", "1111")
    atm.card_init("1111222233334444", "0000")
    
