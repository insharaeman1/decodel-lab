# Expense Tracker
# This program calculates the total amount spent by the user.

total = 0

print("===== EXPENSE TRACKER =====")
print("Enter your expenses one by one.")
print("Type 'done' when you have finished.\n")

while True:
    expense = input("Enter expense amount: ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Please enter a positive amount.")
            continue

        # Accumulator
        total = total + expense

        print(f"Expense added: {expense:.2f}")

    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n===== EXPENSE SUMMARY =====")
print(f"Total Spent: {total:.2f}")
print("============================")