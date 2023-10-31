import os
import subprocess
def main():
    # Intro
    intro = '~~~ Welcome to your terminal checkbook! ~~~'
    print(intro)

    # read the balance from the file if it exists
    if os.path.exists('checkbook_ledger.txt'):
        with open('checkbook_ledger.txt') as f:
            balance_str = f.read()
            balance = float(balance_str)
    else:
        balance = 0.0

    # infinite loop
    while True:
        print('What would you like to do?')
        print(' 1) view current balance \n 2) record a debit (withdraw) \n 3) record a credit (deposit) \n 4) exit')
        user_input = input('Your choice? ')

        # view current balance
        if user_input == '1':
            print(f'your current balance is ${balance: .2f}')

        # add a debit (withdrawal)
        elif user_input == '2':
            try:
                debit = float(input('How much is your debit? $'))
                balance -= debit
            except ValueError:
                print("that's not a valid number")

        # add deposit
        elif user_input == '3':
            try:
                deposit = float(input('How much would you like to deposit? $'))
                balance += deposit
            except ValueError:
                print("that's not a valid number!")
        # exit
        elif user_input == '4':
            print('Thanks, have a great day')
            with open('checkbook_ledger.txt', 'w') as f:
                f.write(str(balance))
            break

        else:
            print('invalid input, please try again')

        # create and update ledger

main()