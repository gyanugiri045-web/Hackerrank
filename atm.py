def ATM():
    balance = 12000
    pin = 123

    entered_pin = int(input("Enter your (3-digit) pin:"))

    if entered_pin != pin:
        print("Incorrect pin!")
        return
    
    while True:
        print("-- select your choice --")
        print("1. check balance")
        print("2. cash withdraw")
        print("3. deposite")
        print("4. exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
           print(f"Your recent balance is: {balance} ")

        elif choice == 2:
            amount = int(input("Enter your amount to withdraw:"))

            if amount > balance:
                print("Insufficient balance!!")
            elif amount == 0:
                print("Invalid amount!")
            else:
                balance -= amount
                print(f"Remening balance is: {balance}")

        elif choice == 3:
            deposite_amount = int(input("Enter amount to deposite:"))
            if deposite_amount<=0:
                print("Invalid amount!!")
            else:
                balance += deposite_amount
                print(f"Your new balance is:{balance}")

        elif choice == 4:
            break

        else:
            print("Invalid choice!!")
            return

ATM()      


        

    