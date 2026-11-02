print("===== SMART CANTEEN =====")
bill_amount = float(input("Enter your total bill amount (Rs.): "))

# Task 1: Invalid bill check
if bill_amount <= 0:
    print("Invalid bill amount! Bill must be greater than zero.")
else:
    # Discount based on bill amount (elif: only one condition runs)
    if bill_amount >= 3000:
        discount_rate = 20
    elif bill_amount >= 2000:
        discount_rate = 10
    elif bill_amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    # Task 2: Membership card gives extra 5% discount
    has_card = input("Do you have a membership card? (yes/no): ").lower()
    if has_card == "yes":
        discount_rate = discount_rate + 5

    discount_amount = bill_amount * discount_rate / 100
    final_amount = bill_amount - discount_amount

    print("\n===== BILL SUMMARY =====")
    print(f"Original Bill: Rs. {bill_amount:.2f}")
    print(f"Discount Rate: {discount_rate}%")
    print(f"Discount Amount: Rs. {discount_amount:.2f}")
    print(f"Final Payable: Rs. {final_amount:.2f}")

    # Task 3: Savings message
    if discount_amount > 0:
        print(f"Congratulations! You saved Rs. {discount_amount:.2f}")
