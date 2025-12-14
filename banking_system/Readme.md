# 🏦 Banking System — Pure Python (No ML, No Advanced Algorithms)

This project is a **file-based banking system** built using **only core Python**.
No machine learning, no deep learning, no fancy algorithms — just **clean logic, safe file handling, and real-world system design**.

It is designed for:

* Beginners who want **clear understanding**
* Students preparing for **viva / exams / interviews**
* Anyone learning **backend-style Python projects**

---

## ✨ Key Features

* Create and manage bank accounts
* Deposit, withdraw, and transfer money
* Secure PIN hashing (PBKDF2)
* Persistent storage using JSON
* Crash-safe database saving
* Automatic backups
* Audit logging (bank-style logs)
* Modular, clean project structure

---

## 🧱 Project Structure

```
banking_system/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   ├── accounts.py        # Account logic (deposit, withdraw, transfer)
│   ├── transactions.py    # Transaction structure
│   └── auth.py            # PIN hashing & verification
│
├── services/
│   ├── __init__.py
│   ├── storage.py         # Safe load/save database
│   └── logger.py          # Audit logging
│
├── data/
│   ├── database.json      # Main database file
│   ├── backup/            # Auto backups
│   └── logs/
│       └── audit.log      # Log file
│
├── tests/
│   ├── test_accounts.py
│   ├── test_auth.py
│   └── test_storage.py
│
└── README.md
```

---

## 🧠 Design Philosophy

This project follows **real software engineering principles**, not academic tricks.

* **Rule-based system**, not algorithm-heavy
* **Separation of concerns** (logic, storage, logging)
* **Defensive programming** (validations everywhere)
* **Crash safety** (temporary files + atomic replace)
* **Auditability** (logs for every action)

---

## 📂 Module Explanation

### 🔹 `app.py`

Main entry point of the program.

* Shows CLI menu
* Takes user input
* Calls core logic

---

### 🔹 `core/accounts.py`

Handles **bank account logic**:

* Create account
* Deposit money
* Withdraw money
* Transfer money
* Maintain transaction history

This file contains **business rules** — no file handling.

---

### 🔹 `core/transactions.py`

Defines how a **transaction is structured**.

* Timestamp
* Type (deposit, withdraw, transfer)
* Amount
* Balance after transaction

Used to keep records consistent and clean.

---

### 🔹 `core/auth.py`

Handles **security**:

* PIN hashing using `hashlib.pbkdf2_hmac`
* PIN verification
* Failed login attempts
* Account lock mechanism

PINs are **never stored in plain text**.

---

### 🔹 `services/storage.py`

Handles **database operations**:

* Load data from JSON
* Save data safely using temp files
* Create automatic backups

Uses **atomic file replace** to avoid corruption.

---

### 🔹 `services/logger.py`

Handles **audit logging**:

* Logs deposits, withdrawals, transfers
* Logs errors and warnings
* Writes logs to `data/logs/audit.log`

Banks rely heavily on logs — this file mimics that behavior.

---

## 💾 Database Design (`database.json`)

Example structure:

```json
{
  "1001": {
    "name": "Divya Singh Shekhawat",
    "balance": 1000,
    "pin": {
      "salt": "...",
      "hash": "...",
      "iterations": 150000
    },
    "failed_attempts": 0,
    "locked_until": null,
    "txns": []
  }
}
```

---

## 🔐 Security Notes

* PINs are hashed using **PBKDF2 + SHA256**
* Random salt prevents rainbow-table attacks
* Constant-time comparison prevents timing attacks
* Account locks after repeated failures

This is **industry-accepted practice**.

---

## 🧪 Testing

Basic unit tests are included in the `tests/` folder.

You can run tests manually or using:

```bash
python -m unittest discover tests
```

---

## 🚀 How to Run

1. Clone or download the project
2. Make sure Python 3.8+ is installed
3. Run the app:

```bash
python app.py
```

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

* Python project structuring
* File handling & persistence
* Secure authentication basics
* Logging and audit trails
* Clean, maintainable backend design

---

## ❌ What This Project Does NOT Use

* No Machine Learning
* No Deep Learning
* No advanced algorithms
* No external frameworks

This keeps the project **simple, explainable, and strong**.

---

## 📌 Ideal For

* College projects
* Python practice
* Backend fundamentals
* Resume project
* Viva / interview explanation

---

## 🧠 One-Line Summary

> A clean, safe, file-based banking system built in pure Python using real-world backend design principles.

---

**Author:** Divya Singh Shekhawat
**Language:** Python
**Type:** Educational / Practice Project

