def main():
    # Intro
    intro = '~~~ Welcome to your terminal checkbook! ~~~'
    print(intro)

    # infinite loop
while True:
    print('What would you like to do?')
    print(' 1) view current balance \n 2) record a debit (withdraw) \n 3) record a credit (deposit) \n 4) exit')
    user_input = input('Your choice? ')
    print(user_input)
    # view current balace
    if user_input == '1':
        print(f'your current balance is {}')

    # add a debit (withdrawal)
    elif user_input == '2':

    # add deposit
    elif user_input == '3':

    # exit
    elif user_input == '4':
        print('Thanks, have a great day')

    else:
        print('invalid input, please try againg')
    # create and update ledger
    
main()
