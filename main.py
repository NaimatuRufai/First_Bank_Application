from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\nWelcome to NAIMA.BANK APP PLC\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your preferred option: ")
        
        # We have to write a conditional statement for all five options above
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            name = input("Enter your account name: ")
            amount = float(input("Enter initial deposit amount: "))
            bank.deposit(name, amount)

        elif choice == "3":
            name = input("Enter your account name: ")
            amount = float(input("Enter your withdrawal amount: "))
            bank.withdraw(name, amount)

        elif choice == "4":
            name = input("Enter your account name: ")
            bank.check_balance(name)

        elif choice == "5":
            print("Thank you for banking with us")
            break
        else:
            print("Invalid option entered. Please try again")

if __name__ == main():
    main()

