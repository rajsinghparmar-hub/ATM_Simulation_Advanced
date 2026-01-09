print("your by default pin is: 1234 \nAfter using the program you can also change it\nThank you")
initial_values = 0
starting_balance = 10000

default_PIN = "1234"
maximum_PIN_attempts = 3

attempts_count = 0
daily_withdrawal_limit = 50000

today_withdrawal_track = 0
transaction_history = []

while attempts_count < maximum_PIN_attempts:
    usr_pin = input("enter the pin: ")
    if usr_pin == default_PIN:
        print("PIN verified successfully")
        break
    else:
        attempts_count += 1
        print("wrong pin")
        
if attempts_count == maximum_PIN_attempts:
    print("Card block")
    exit()
    
while True:
    print("OPTIONS:")
    print("1 for Check_balance: ")
    print("2 for Check_Deposit: ")
    print("3 for Check_Withdraw: ")
    print("4 for Change_PIN: ")
    print("5 for Transaction_History: ")
    print("6 for Exit: ")
    
    usr_choice = int(input("enter your option: "))
    if usr_choice == 1:
        print(starting_balance)
            
    elif usr_choice == 2:
        amounts = int(input("enter the amount: "))
        if amounts > 0:
            starting_balance += amounts
            transaction_history.append(f"deposit {amounts}")
        
    elif usr_choice == 3:
        amounts = int(input("enter the amount: "))
        if amounts > 0 and amounts <= starting_balance and amounts <=  daily_withdrawal_limit:
            starting_balance -= amounts
            today_withdrawal_track = amounts
            transaction_history.append(f"withdrawal {amounts}")

        else:
            print(f"your current balance is too low: {starting_balance}\nplease enter a valid amount")    

    elif usr_choice == 4:
        s1 = input("enter your old pin: ")
        if s1 == default_PIN:
            s2 = input("enter the new pin: ")
            default_PIN = s2
            print("Pin succesfully change")
        else:
            print("wrong pin\nTry again ")
    elif usr_choice == 5:
        if not transaction_history:
            print("No transactions")
            print(f"Your current balance is: {starting_balance}")
        else:
            for s3 in transaction_history:
                print(s3)
                
    elif usr_choice == 6:
        print(f"Your current balance is: {starting_balance}")
        print("thank you for using atm")
        break
    