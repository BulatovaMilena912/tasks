class BankAccount:
    def __init__(self, balance, number, nickname):
        self.__balance = balance
        self.__number = number
        self.__nickname = nickname

    @property
    def balance(self):
        return self.__balance

    @property
    def number(self):
        return self.__number

    @property
    def nickname(self):
        return self.__nickname

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def withdraw(self, amount):
        if self.balance <= 0:
            return
        else:
            self.balance -= amount
        return f"Вывели {amount}. Осталось {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Добавили {amount}. Всего {self.balance} на счету"
