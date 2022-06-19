class Bank:
    def __init__(self, db):
        self.db = db
    
    def check_pin(self, card_num, pin_num):
        if card_num in self.db and self.db[card_num]["pin_num"] == pin_num:
            return self.db[card_num]["account"]
        
        else:
            return False


    def check_account(self, card_num, account):
        if account not in self.db[card_num]["account"]:
            return False
        
        return True


    def get_balance(self, card_num, account):
        if not self.check_account(card_num, account):
            return False, "Invalid Account"

        return True, self.db[card_num]["account"][account]


    def deposit(self, card_num, account, amount):
        if not self.check_account(card_num, account):
            return False, "Invalid Account"
        
        self.db[card_num]["account"][account] += amount
        return True, self.db[card_num]["account"][account]


    def withdraw(self, card_num, account, amount):
        if not self.check_account(card_num, account):
            return False, "Invalid Account"
        
        if self.db[card_num]["account"][account] < amount:
            return False, "Not Enough Balance"
        
        self.db[card_num]["account"][account] -= amount
        return True, self.db[card_num]["account"][account]