# 🍽️ Smart Canteen Billing System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-green)
![Topic](https://img.shields.io/badge/Topic-if--elif--else-orange)

A simple Python program that calculates a canteen bill, applies discounts, and shows a clean bill summary.
Made as a class practice project to learn **conditional statements**.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | 🚫 Invalid Bill Check | Bill `<= 0` shows an error message |
| 2 | 🎟️ Membership Card | Extra **5%** discount for card holders |
| 3 | 🎉 Savings Message | Shows "Congratulations! You saved Rs. X" |
| 4 | 💸 Slab Discount | Discount depends on the bill amount |

---

## 📊 Discount Slabs

| Bill Amount (Rs.) | Discount |
|-------------------|----------|
| 3000 and above    | 20% |
| 2000 – 2999       | 10% |
| 1000 – 1999       | 5%  |
| Below 1000        | 0%  |
| Membership Card   | +5% extra |

---

## 🔄 Program Flow

```
Enter Bill
    │
    ▼
Bill <= 0? ──Yes──► ❌ Invalid Bill
    │No
    ▼
Check Slab (if / elif / else)
    │
    ▼
Membership Card? ──Yes──► +5% discount
    │
    ▼
Calculate Final Amount
    │
    ▼
Show Bill Summary
    │
    ▼
Discount > 0? ──Yes──► 🎉 Congratulations message
```

---

## ▶️ How to Run

```bash
python smart_canteen.py
```

---

## 🖥️ Demo

### ✅ Example 1: Bill with membership card

```
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 2500
Do you have a membership card? (yes/no): yes

===== BILL SUMMARY =====
Original Bill: Rs. 2500.00
Discount Rate: 15%
Discount Amount: Rs. 375.00
Final Payable: Rs. 2125.00
Congratulations! You saved Rs. 375.00
```

### ✅ Example 2: No discount

```
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 500
Do you have a membership card? (yes/no): no

===== BILL SUMMARY =====
Original Bill: Rs. 500.00
Discount Rate: 0%
Discount Amount: Rs. 0.00
Final Payable: Rs. 500.00
```

### ❌ Example 3: Invalid bill

```
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): -100
Invalid bill amount! Bill must be greater than zero.
```

---

## 🧠 Teaching Question

**Why do we use `elif` instead of several independent `if` statements?**

With `elif`, Python stops at the first true condition, so only one discount is applied.
With separate `if` statements, every condition is checked, so a bill of Rs. 3500 would match all three and the wrong discount could be applied.

---

## 📚 What I Learned

- `if`, `elif`, `else` statements
- Taking user input with `input()`
- Type conversion with `float()`
- f-strings and number formatting (`:.2f`)
- Nested conditions

---

## 👤 Author

Made by Malik Usama Awan as part of Python class practice.
