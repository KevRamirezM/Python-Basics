# Python banking program

def ShowBalance(balance):
    print(f"Your balance is: ${balance:.2f}")
    pass

def Deposit():
    amount = float(input("Enter an amount: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def Withdraw(balance):
    amount = input("Enter amount to be withdrawn: ")
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    pass

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            ShowBalance()
        elif choice == "2":
            balance += Deposit()
            print(f"Your new balance is: {balance}")
        elif choice == "3":
            balance += Withdraw()
            print(f"Your new balance is: {balance}")
        elif choice == "4":
            is_running = False
        else:
            print("Invalid number")

    print("Thanks for using this program.")

if __name__ == '__main__':
    main()