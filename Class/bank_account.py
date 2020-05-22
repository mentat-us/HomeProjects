class BankAccount:
    def __init__(self, id, balance=0):
        """

        :param id: str
        :param balance: float
        """

        self.owner = id
        self.__balance = balance

    def deposit(self, cash):
        self.__balance += cash

    def withdrawl(self, cash):
        self.__balance -= cash

    def get_balance(self):
        return self.__balance


    def __str__(self):
        ret_val = self.owner + " hesabin bakiyesi = " + str(self.balance)
        return ret_val


account_can = BankAccount("Can", 12_340_000)
account_can.withdrawl(340_000)
print(account_can)

account_onur = BankAccount("Onur", 90_999_467)
account_onur.withdrawl(999_467)
print(account_onur)