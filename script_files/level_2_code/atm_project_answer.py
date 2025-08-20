Balance = 1000
pin = 1234

print("Welcome to Python ATM!")

pin_num = int(input("enter the atm pin:"))
if pin_num != pin:
    print("Wrong PIN. Exiting...")
else:
    while True:
        print("\n-------------Menu-----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your balance is: {Balance}")

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            Balance += amount
            print(f"{amount} deposited. New_balance: {Balance}")
        elif choice == 3:
            amount = int(input("Enter withdrawal money: "))
            if Balance <= amount:
                print("insufficient funds.")
            else:
                Balance -= amount
                print(f"{amount} withdrawal, Available Balance {Balance}")
        elif choice == 4:
            print("Thank you for using python ATM, Bye")
            break
        else:
            print("Invalid choice, try again!")