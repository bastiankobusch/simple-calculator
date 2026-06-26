balance = 0

#Menu options
while True:
    print("\n===== BANK MENU =====")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Quit")

    choice = input("Choose an option: ")

#Check balance 
    if choice == "1":
        print("Your balance is:", balance)

#Deposit money
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

#Withdraw money
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Not enough balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            print("Withdrawn:", amount)

#Quit
    elif choice == "4":
        print("Goodbye!")
        break

#Invalid option
    else:
        print("Invalid option, choose 1-4")