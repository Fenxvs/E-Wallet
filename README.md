# 🏦 Console Digital Wallet

> 🎓 **A Python training project** built to practice and solidify core programming concepts through a real-world inspired use case.

A simple command-line banking application built with Python that simulates core banking operations including account registration, authentication, balance management, deposits, withdrawals, and transfers.

This project was developed as a **hands-on learning exercise** to understand how Python is used to build functional, data-driven applications from scratch — without relying on external frameworks or libraries.

---

## 📋 Features

- **User Registration** — Create a new account with a username, password, and starting balance
- **Authentication** — Secure login with username and password validation
- **Balance Check** — View your current account balance
- **Deposit** — Add funds to your account
- **Withdraw** — Withdraw funds with insufficient balance protection
- **Transfer** — Send money to other registered users
- **Persistent Storage** — All data is saved to a local JSON file

---

## 🧠 Python Concepts Practiced

This project was built specifically to apply and reinforce the following core Python concepts:

| Concept | How It's Used |
|---|---|
| **Functions** | Each banking operation (`deposit`, `withdraw`, `transfer`, etc.) is isolated in its own function |
| **File I/O** | Reading and writing `database.json` using Python's built-in `open()` and `json` module |
| **JSON Handling** | Parsing and updating structured data with `json.load()` and `json.dump()` |
| **Control Flow** | `while` loops, `if/elif/else` chains power the entire CLI menu system |
| **Exception Handling** | `try/except` blocks catch invalid user input (e.g. non-numeric amounts) |
| **String Methods** | `.strip()` for sanitizing user input |
| **Type Casting** | Converting input strings to `float` for numeric operations |
| **Data Structures** | Lists of dictionaries represent the user database in memory |
| **Modules** | Using `json` and `hashlib` from the Python standard library |

> Building a banking system — even a simple one — touches almost every fundamental concept taught in beginner-to-intermediate Python. That's exactly why this project was chosen as a training ground.

---

## 🗂️ Project Structure

```
celestial-jr/
├── main.py           # Main application logic & CLI interface
├── database.json     # JSON-based data store for user accounts
└── README.md
```

---

## 🗄️ Data Storage

User data is stored locally in `database.json` in the following format:

```json
{
  "users": [
    {
      "username": "example",
      "password": "yourpassword",
      "balance": 1000.0
    }
  ]
}
```

> ⚠️ **Note:** Passwords are currently stored in plain text. This project is intended for educational purposes only and is **not suitable for production use**.

---
