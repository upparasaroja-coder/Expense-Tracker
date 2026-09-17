print("===== Expense Tracker =====")
expenses = []
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\n===== Expenses =====")

            for expense in expenses:
                print("Name:", expense[0])
                print("Amount:", expense[1])
                print("-------------------")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total Expense:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")