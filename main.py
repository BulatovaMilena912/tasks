from bank_account import BankAccount

if __name__ == "__main__":
    milena = BankAccount(0, "Sberbank", "Milya")
    print(f"{milena.nickname} имеет на счету {milena.number} {milena.balance}")
    message = milena.withdraw(8000)
    print(message)

    notification = milena.deposit(13000)
    print(notification)
