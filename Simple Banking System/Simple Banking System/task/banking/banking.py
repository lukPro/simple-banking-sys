import random


class BankAccount:
    all_accounts = []

    def __init__(self):
        self.balance = 0
        self.account_number = None
        self.account_pin = None
        BankAccount.all_accounts.append(self)

    def set_number(self):
        self.account_number = int('400000' + str(random.randrange(100000000, 10 ** 9)) + '1')

    def set_pin(self):
        self.account_pin = random.randrange(1000, 9999)

    def get_info(self):
        print('Your card has been created')
        print('Your card number:')
        print(self.account_number)
        print('Your card PIN:')
        print(self.account_pin)


def welcome_menu():
    print('')
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    print('')


def account_menu():
    print('')
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    print('')


stop_cond = False

while not stop_cond:
    welcome_menu()
    option = int(input())

    if option == 1:
        account = BankAccount()
        account.set_number()
        account.set_pin()
        account.get_info()
    elif option == 2:
        print('Enter your card number:')
        tmp_account_number = int(input())
        for account in BankAccount.all_accounts:
            if account.account_number == tmp_account_number:
                print('Enter your PIN:')
                tmp_pin = int(input())
                if account.account_pin == tmp_pin:
                    print('You have successfully logged in!')
                    tmp_stop_cond = False
                    while not tmp_stop_cond:
                        account_menu()
                        tmp_option = int(input())
                        if tmp_option == 1:
                            print(account.balance)
                        elif tmp_option == 2:
                            print('You have successfully logged out!')
                        elif tmp_option == 0:
                            tmp_stop_cond = True
                            stop_cond = True
                            break
                else:
                    print('Wrong card number or PIN!')
            else:
                print('Wrong')

    elif option == 0:
        stop_cond = True

print('Bye!')
