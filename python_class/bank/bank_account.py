from typing import List


class BankAccount:
    account_numbers: List[int] = []
    last_account_number: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = 0
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.__account_number = an
        self.account_numbers.append(an)

    def display(self) -> None:
        print(f"Your current balance : {self.balance}")
        print()

    def deposit(self) -> None:
        amount_deposit = float(input(f"please enter your amount of cash {self.name}: "))
        self.balance += amount_deposit
        print("Success!!")
        print()

    def withdraw(self):
        amount_withdraw = float(input(f"please enter your amount of cash {self.name}: "))
        if amount_withdraw > self.balance:
            print("insufflation Balance!")
        else:
            self.balance -= amount_withdraw
            print("Success!!")
        print()


def creat_account(name_account: str) -> BankAccount:
    return BankAccount(name_account)


def menu_bank() -> int:
    choose = int(input("1) Display your Account information\n"
                       "2) Deposit\n"
                       "3) Withdraw\n"
                       "4) Exit\n"
                       ":"))
    return choose


def main():
    select = int(input("hi sir ,\nSelect 1 for Creat new account\nSelect 2 for Exist\n:"))
    if select == 1:
        name = input("Enter your name :")
        account = creat_account(name)
        print(20 * "*", f"Welcome To Amin Bank {account.name}", 20 * "*")
        while True:
            choose_menu = menu_bank()
            if choose_menu == 1:
                account.display()
            elif choose_menu == 2:
                account.deposit()
            elif choose_menu == 3:
                account.withdraw()
            else:
                break
    print("Good Luck")


if __name__ == "__main__":
    main()
