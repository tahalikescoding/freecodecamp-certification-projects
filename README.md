# freeCodeCamp Certification Projects 🐍

All the certification projects and labs from the freeCodeCamp Python certification course.

## 📂 Projects

### Certification Project 1. User Config Manager
`useronfigmanager.py`

A simple settings manager that lets you add, update, delete, and view user configuration settings stored in a dictionary. Built around string formatting, dictionary operations, and key/value normalization.

**Functions:**

- **`add_setting(settings, key_value)`**
  Adds a new setting to the dictionary.
  - Converts both key and value to lowercase before storing
  - Fails gracefully if the key already exists, without overwriting it
  - Returns a success or error message accordingly

- **`update_setting(settings, key_value)`**
  Updates the value of an existing setting.
  - Converts both key and value to lowercase
  - Fails gracefully if the key doesn't exist yet
  - Returns a success or error message accordingly

- **`delete_setting(settings, key)`**
  Removes a setting from the dictionary.
  - Converts the key to lowercase before checking/removing
  - Returns a success message if deleted, or an error if not found

- **`view_settings(settings)`**
  Displays all current settings.
  - Returns `"No settings available."` if the dictionary is empty
  - Otherwise returns a formatted, multi-line summary with each key capitalized

### Certification Project 2. Budget App

A command-line budgeting tool built with Python. Create spending categories, track deposits and withdrawals, transfer funds between categories, and visualize spending with a bar chart.

## Features

- **Category class** — create a budget category (e.g. Food, Clothing, Entertainment)
  - `deposit(amount, description)` — add funds
  - `withdraw(amount, description)` — remove funds (returns `False` if insufficient funds)
  - `get_balance()` — current balance
  - `transfer(amount, other_category)` — move funds to another category (returns `False` if it fails)
  - `check_funds(amount)` — check if a withdrawal/transfer is affordable
  - `__str__` — prints a formatted ledger:
    ```
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    Total: 989.85
    ```

- **`create_spend_chart(categories)`** — generates a bar chart (as a string) showing percentage spent per category, rounded down to the nearest 10%:
    ```
    Percentage spent by category
    100|
     90|
     80|
     70|
     60|
     50|
     40|
     30|          o
     20|          o
     10|  o       o
      0|  o       o
        ----------
         F        E
         o        n
         o        t
         d        e
                  r
                  t
                  a
                  i
                  n
                  m
                  e
                  n
                  t
    ```

## Usage

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(35.55, "movies")

food.transfer(50, entertainment)

print(food)
print(create_spend_chart([food, entertainment]))
```

### Certification Project 3. Rectangle / Square Calculator (OOP Inheritance)

A freeCodeCamp Scientific Computing certification project demonstrating class inheritance in Python. Implements a `Rectangle` class and a `Square` subclass that inherits and overrides its parent's behavior.

## Classes

### `Rectangle`

Created with a `width` and `height`.

| Method | Description |
|---|---|
| `set_width(value)` | Sets the width. Raises `ValueError` for negative or non-numeric input. |
| `set_height(value)` | Sets the height. Same validation as above. |
| `get_area()` | Returns `width × height`. |
| `get_perimeter()` | Returns `2 × (width + height)`. |
| `get_diagonal()` | Returns `√(width² + height²)`. |
| `get_picture()` | Returns an ASCII-art string of `*` characters — `height` rows of `width` stars each. Returns `"Too big for picture."` if either dimension exceeds 50. |
| `get_amount_inside(shape)` | Returns how many times another shape's area fits inside this one's area. |
| `__repr__` | `Rectangle(width=5, height=10)` |

### `Square(Rectangle)`

Subclasses `Rectangle`. Created with a single `length`, which sets both `width` and `height` via `super().__init__()`.

| Method | Description |
|---|---|
| `set_width(value)` | Overridden — sets **both** width and height to keep it square. |
| `set_height(value)` | Overridden — same behavior as `set_width`. |
| `set_side(value)` | Sets both width and height directly. |
| `__repr__` | Overridden — `Square(side=9)` |

All of `Rectangle`'s other methods (`get_area`, `get_perimeter`, `get_diagonal`, `get_picture`, `get_amount_inside`) are inherited unchanged, since a square's area/perimeter/diagonal math works identically once width and height are equal.



## 🛠️ Tech Stack
- Python 3
- Core dictionary and string manipulation (no external libraries)

## 📌 Status
Actively adding new certification projects as I progress through the course.
