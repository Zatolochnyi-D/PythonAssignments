class Account:
    def __init__(self, userId):
        self.__balance = 0
        self.__userId = userId

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

acc = Account(0)
acc.set_balance(10)
print(acc.get_balance()) # Expected: 10
acc.__balance            # Expected: AttributeError