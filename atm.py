from bank import Bank


class ATM:
    def __init__(self, bank, cash_bin):
        self.bank = bank
        self.cash_bin = cash_bin
        self.user_card = None
        self.user_accounts = None
        self.selected_account = None


    def card_insert(self, card_num):
        if self.user_card is not None:
            return False

        if len(card_num) != 16:
            return False
        
        if not card_num.isdigit():
            return False
        
        self.user_card = card_num
        return True


    def pin_check(self, pin_num):
        if self.user_card is None:
            return False, "Card is not inserted"

        if len(pin_num) != 4:
            self.return_card()
            return False, "PIN number should be 4 digits long"
        
        if not pin_num.isdigit():
            self.return_card()
            return False

        res = self.bank.check_pin(self.user_card, pin_num)
        if not res:
            self.return_card()
            return False, "Wrong Card number / PIN number"
        
        self.user_accounts = res
        return True, self.user_accounts


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