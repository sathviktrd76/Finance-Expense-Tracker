# SMART FINANCE EXPENSE TRACKER

# DAY 2 - Operators, Type Conversion & Calculations

print("==== Smart Finance Expense Tracker ====")

# Get the first expense
category1 = input("\nEnter first expense category: ")
amount1 = float(input("Enter first expense amount: "))

# Get the second expense
category2 = input("\nEnter second expense category: ")
amount2 = float(input("Enter second expense amount: "))

# Get the third expense
category3 = input("\nEnter third expense category: ")
amount3 = float(input("Enter third expense amount: "))

# Calculate total spending
total_spending = amount1 + amount2 + amount3

# Calculate average spending
average = total_spending / 3

# Display expense details
print("\n---- Expense Details ----")

print("\nFirst Expense:")
print("Category:", category1)
print("Amount: ₹", amount1)

print("\nSecond Expense:")
print("Category:", category2)
print("Amount: ₹", amount2)

print("\nThird Expense:")
print("Category:", category3)
print("Amount: ₹", amount3)

print("\nTotal Spending: ₹", total_spending)
print(f"Average Spending: ₹{average:.2f}")