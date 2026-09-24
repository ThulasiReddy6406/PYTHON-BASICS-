print("========================================")
print("          WELCOME TO SANDRA ATM")
print("========================================")


# ---------------- PIN LOGIN ----------------

correct_pin = 6406
attempts = 3

while attempts > 0:

    pin = int(input("Enter your PIN :- "))

    if pin == correct_pin:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print(f"Wrong PIN! Attempts remaining: {attempts}")
            continue
        else:
            print("Too many wrong attempts!")
            print("Your account is blocked.")
            break


# Only continue if PIN is correct
if attempts > 0:

    current_balance = 250000

    transaction_history = []

    while True:

        print("\n========================================")
        print("              ATM MENU")
        print("========================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        print("========================================")

        choice = int(input("Enter your choice :- "))

        # ---------------- CHECK BALANCE ----------------

        if choice == 1:

            print(f"\nCurrent Balance: ₹{current_balance}")


        # ---------------- DEPOSIT ----------------

        elif choice == 2:

            deposit = int(input("Enter deposit amount :- "))

            if deposit <= 0:
                print("Invalid amount!")
                print("Deposit amount must be greater than 0.")
                continue

            current_balance += deposit

            transaction_history.append(
                f"Deposit  : ₹{deposit}"
            )

            print(f"₹{deposit} deposited successfully.")
            print(f"New Balance: ₹{current_balance}")


        # ---------------- WITHDRAW ----------------

        elif choice == 3:

            withdraw = int(input("Enter withdrawal amount :- "))

            if withdraw <= 0:
                print("Invalid amount!")
                print("Withdrawal amount must be greater than 0.")
                continue

            if withdraw > current_balance:
                print("Insufficient balance!")
                continue

            current_balance -= withdraw

            transaction_history.append(
                f"Withdraw : ₹{withdraw}"
            )

            print(f"₹{withdraw} withdrawn successfully.")
            print(f"Remaining Balance: ₹{current_balance}")


        # ---------------- CHANGE PIN ----------------

        elif choice == 4:

            old_pin = int(input("Enter old PIN :- "))

            if old_pin != correct_pin:

                print("Incorrect old PIN!")
                continue

            new_pin = int(input("Enter new PIN :- "))
            confirm_pin = int(input("Confirm new PIN :- "))

            if new_pin != confirm_pin:

                print("New PIN and confirmation PIN do not match.")
                continue

            if new_pin == correct_pin:

                print("New PIN cannot be the same as old PIN.")
                continue

            correct_pin = new_pin

            print("PIN changed successfully!")


        # ---------------- TRANSACTION HISTORY ----------------

        elif choice == 5:

            print("\n========= TRANSACTION HISTORY =========")

            if len(transaction_history) == 0:

                print("No transactions yet.")

            else:

                for transaction in transaction_history:
                    print(transaction)

            print("=======================================")


        # ---------------- EXIT ----------------

        elif choice == 6:

            print("\nThank you for using Sandip ATM.")
            print("Have a nice day!")
            break


        # ---------------- INVALID CHOICE ----------------

        else:

            print("Invalid choice!")
            print("Please enter a number between 1 and 6.")
            continue


else:

    # Future feature
    pass