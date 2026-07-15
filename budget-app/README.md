# 💰 Budget App

A simple Python budget management application that allows users to
manage expenses across different categories, transfer funds, and
visualize spending using a text-based percentage chart.

This project was built as part of the **freeCodeCamp Scientific
Computing with Python** certification.

------------------------------------------------------------------------

## 📌 Features

-   Create multiple budget categories
-   Deposit funds into a category
-   Withdraw funds with balance validation
-   Transfer money between categories
-   Check available funds before transactions
-   View formatted transaction history
-   Generate a spending percentage bar chart

------------------------------------------------------------------------

## 🚀 Technologies Used

-   Python 3
-   Object-Oriented Programming (OOP)

------------------------------------------------------------------------

## 📂 Project Structure

``` text
budget-app/
│
├── budget.py
├── test_module.py
├── README.md
```

## 🛠️ How It Works

### Create Categories

``` python
from budget import Category
food = Category("Food")
clothing = Category("Clothing")
```

### Deposit

``` python
food.deposit(1000, "Initial Deposit")
```

### Withdraw

``` python
food.withdraw(50.25, "Groceries")
```

### Transfer

``` python
food.transfer(100, clothing)
```

### Spending Chart

``` python
from budget import create_spend_chart
print(create_spend_chart([food, clothing]))
```

## 🏗️ Category Methods

  Method            Description
  ----------------- -----------------------------
  `deposit()`       Add money
  `withdraw()`      Remove money if funds exist
  `transfer()`      Transfer funds
  `get_balance()`   Current balance
  `check_funds()`   Verify available funds

## 🧪 Testing

Designed to pass all required freeCodeCamp unit tests.

## ▶️ Run

``` bash
python budget.py
```

## 📄 License

Educational project for the freeCodeCamp Scientific Computing with
Python curriculum.
