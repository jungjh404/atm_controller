from bank import Bank


class ATM:
    def __init__(self, bank, cash_bin):
        self.bank = bank
        self.cash_bin = cash_bin
        self.user_card = None
        self.user_accounts = None
        self.selected_account = None


    def card_init(self, card_num, pin_num):
        res = self.bank.check_pin(card_num, pin_num)
        if not res:
            return False
        
        self.user_card = card_num
        self.user_accounts = res
        return True


    def get_account(self):
        return self.user_accounts


    def select_account(self, account):
        if account in self.user_accounts:
            self.selected_account = account
            return True

        return False


    def return_card(self):
        self.user_card = None
        self.user_accounts = None
        self.selected_account = None


    def balance(self):
        res = self.bank.get_balance(self.user_card, self.selected_account)
        self.return_card()
        return res


    def deposit(self, amount):
        res = self.bank.deposit(self.user_card, self.selected_account, amount)
        
        if not res[0]:
            return res

        self.cash_bin += amount
        self.return_card()
        return res


    def withdraw(self, amount):
        if self.cash_bin < amount:
            return False, "Not Enough Cash Bin"
        
        res = self.bank.withdraw(self.user_card, self.selected_account, amount)
        if not res[0]:
            return res

        self.cash_bin -= amount
        self.return_card()
        return res