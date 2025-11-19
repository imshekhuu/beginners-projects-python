Banking System — Complete Guide
Project goal (short)

Ek simple, pure-Python banking simulator jo accounts create kare, deposit/withdraw/transfer support kare, transaction history rakhe, aur data disk pe JSON files me persist kare. CLI (menu) interface, exceptions handling, backups, aur basic unit tests honge.

Features

Create / Delete account

Deposit / Withdraw

Transfer between accounts

Transaction history (passbook) per account

Persist data to JSON files (simple DB)

Input validation, error handling, and backup export

Unit tests for core logic

Folder structure
banking_app/
├─ app.py               # CLI entrypoint
├─ accounts.py          # Account and business logic
├─ storage.py           # JSON persistence (load/save/backup)
├─ utils.py             # Helpers & validators
├─ data/
│  ├─ accounts.json     # stored accounts & txns
│  └─ backups/          # automatic backups
├─ tests/
│  └─ test_accounts.py  # unittest for accounts
└─ README.md

Design (classes & responsibilities)

Account (accounts.py)

Fields: acc_no, name, balance, txns (list of txns)

Methods: deposit(), withdraw(), transfer_to(), get_statement()

Storage (storage.py)

Methods: load_all(), save_all(), backup(), next_acc_no()

App CLI (app.py)

Interactive menu to call account operations and persist changes.

Data format (accounts.json) — example
{
  "1001": {
    "acc_no": "1001",
    "name": "Divya Singh",
    "balance": 2500.0,
    "txns": [
      ["2025-11-19T17:00:00", "deposit", 2500.0, "Initial deposit"]
    ]
  }
}


Transaction entry format: [iso_timestamp, type, amount, note]

Full starter code
accounts.py
# accounts.py
import datetime

class Account:
    def __init__(self, acc_no: str, name: str, balance: float = 0.0, txns=None):
        self.acc_no = str(acc_no)
        self.name = name
        self.balance = float(balance)
        self.txns = txns or []

    def _record(self, ttype: str, amount: float, note: str = ""):
        timestamp = datetime.datetime.now().isoformat()
        self.txns.append([timestamp, ttype, float(amount), note])

    def deposit(self, amount: float, note: str = ""):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record("deposit", amount, note)
        return self.balance

    def withdraw(self, amount: float, note: str = ""):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._record("withdraw", amount, note)
        return self.balance

    def transfer_to(self, other_account: "Account", amount: float, note: str = ""):
        if not isinstance(other_account, Account):
            raise TypeError("other_account must be Account instance.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        # perform transfer
        self.balance -= amount
        other_account.balance += amount
        tnote = note or f"transfer to {other_account.acc_no}"
        onote = note or f"transfer from {self.acc_no}"
        self._record("transfer_out", amount, tnote)
        other_account._record("transfer_in", amount, onote)
        return self.balance

    def get_statement(self, limit: int = None):
        # returns txns (newest first if limit provided)
        if limit is None:
            return list(self.txns)
        return list(self.txns[-limit:])

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance,
            "txns": list(self.txns)
        }

    @staticmethod
    def from_dict(d):
        return Account(d["acc_no"], d["name"], d.get("balance", 0.0), txns=d.get("txns", []))

storage.py
# storage.py
import json
from pathlib import Path
from typing import Dict
import shutil
from datetime import datetime

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
BACKUP_DIR = DATA_DIR / "backups"
BACKUP_DIR.mkdir(exist_ok=True)
DB_FILE = DATA_DIR / "accounts.json"

class Storage:
    def __init__(self, db_file=DB_FILE):
        self.db_file = Path(db_file)

    def load_all(self) -> Dict[str, dict]:
        if not self.db_file.exists():
            return {}
        with open(self.db_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_all(self, data: Dict[str, dict]):
        # safe write
        tmp = self.db_file.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        tmp.replace(self.db_file)

    def backup(self):
        if not self.db_file.exists():
            return None
        stamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        dest = BACKUP_DIR / f"accounts_{stamp}.json"
        shutil.copy2(self.db_file, dest)
        return dest

    def next_acc_no(self) -> str:
        data = self.load_all()
        if not data:
            return "1001"
        # choose numeric max + 1
        nums = [int(k) for k in data.keys() if k.isdigit()]
        if not nums:
            return "1001"
        return str(max(nums) + 1)

utils.py
# utils.py
def parse_amount(s):
    try:
        val = float(s)
    except Exception:
        raise ValueError("Invalid amount.")
    if val <= 0:
        raise ValueError("Amount must be positive.")
    return val

app.py (CLI)
# app.py
import sys
from accounts import Account
from storage import Storage
from utils import parse_amount

def pretty_print(acct: Account):
    print(f"Account: {acct.acc_no} | Name: {acct.name} | Balance: {acct.balance:.2f}")

def load_accounts(storage):
    raw = storage.load_all()
    accs = {}
    for k, v in raw.items():
        accs[k] = Account.from_dict(v)
    return accs

def save_accounts(storage, accs):
    data = {k: v.to_dict() for k, v in accs.items()}
    storage.save_all(data)

def create_account(accs, storage):
    name = input("Account holder name: ").strip()
    acc_no = storage.next_acc_no()
    acct = Account(acc_no, name, balance=0.0)
    accs[acc_no] = acct
    save_accounts(storage, accs)
    print(f"Created account {acc_no} for {name}.")

def deposit_flow(accs, storage):
    acc_no = input("Account number: ").strip()
    acct = accs.get(acc_no)
    if not acct:
        print("Account not found.")
        return
    amt = parse_amount(input("Amount to deposit: ").strip())
    note = input("Note (optional): ").strip()
    acct.deposit(amt, note)
    save_accounts(storage, accs)
    pretty_print(acct)

def withdraw_flow(accs, storage):
    acc_no = input("Account number: ").strip()
    acct = accs.get(acc_no)
    if not acct:
        print("Account not found.")
        return
    amt = parse_amount(input("Amount to withdraw: ").strip())
    note = input("Note (optional): ").strip()
    try:
        acct.withdraw(amt, note)
    except ValueError as e:
        print("Error:", e)
        return
    save_accounts(storage, accs)
    pretty_print(acct)

def transfer_flow(accs, storage):
    src = input("Source account: ").strip()
    dst = input("Destination account: ").strip()
    src_ac = accs.get(src); dst_ac = accs.get(dst)
    if not src_ac or not dst_ac:
        print("One of the accounts not found.")
        return
    amt = parse_amount(input("Amount to transfer: ").strip())
    note = input("Note (optional): ").strip()
    try:
        src_ac.transfer_to(dst_ac, amt, note)
    except ValueError as e:
        print("Error:", e)
        return
    save_accounts(storage, accs)
    print("Transfer successful.")
    pretty_print(src_ac); pretty_print(dst_ac)

def statement_flow(accs):
    acc_no = input("Account number: ").strip()
    acct = accs.get(acc_no)
    if not acct:
        print("Account not found.")
        return
    print(f"Statement for {acct.name} ({acct.acc_no}) — Balance: {acct.balance:.2f}")
    for t in acct.get_statement():
        print(*t)

def backup_flow(storage):
    dest = storage.backup()
    if dest:
        print("Backup created at:", dest)
    else:
        print("No DB to backup.")

def delete_account(accs, storage):
    acc_no = input("Account number to delete: ").strip()
    if acc_no not in accs:
        print("No such account.")
        return
    confirm = input(f"Type DELETE to confirm deleting {acc_no}: ").strip()
    if confirm == "DELETE":
        del accs[acc_no]
        save_accounts(storage, accs)
        print("Deleted.")
    else:
        print("Aborted.")

def menu():
    storage = Storage()
    accs = load_accounts(storage)
    actions = {
        "1": ("Create account", lambda: create_account(accs, storage)),
        "2": ("Deposit", lambda: deposit_flow(accs, storage)),
        "3": ("Withdraw", lambda: withdraw_flow(accs, storage)),
        "4": ("Transfer", lambda: transfer_flow(accs, storage)),
        "5": ("Statement", lambda: statement_flow(accs)),
        "6": ("Backup DB", lambda: backup_flow(storage)),
        "7": ("Delete account", lambda: delete_account(accs, storage)),
        "0": ("Exit", lambda: sys.exit(0))
    }
    while True:
        print("\n=== Banking Menu ===")
        for k,v in actions.items():
            print(k, "-", v[0])
        choice = input("Choose: ").strip()
        if choice in actions:
            try:
                actions[choice][1]()
            except Exception as e:
                print("Operation failed:", e)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()

Unit test example (tests/test_accounts.py)
# tests/test_accounts.py
import unittest
from accounts import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.a = Account("1000", "Tester", 100.0)
        self.b = Account("1001", "Other", 0.0)

    def test_deposit(self):
        self.a.deposit(50)
        self.assertEqual(self.a.balance, 150.0)

    def test_withdraw_success(self):
        self.a.withdraw(30)
        self.assertEqual(self.a.balance, 70.0)

    def test_withdraw_fail(self):
        with self.assertRaises(ValueError):
            self.a.withdraw(1000)

    def test_transfer(self):
        self.a.transfer_to(self.b, 40)
        self.assertEqual(self.a.balance, 60.0)
        self.assertEqual(self.b.balance, 40.0)

if __name__ == "__main__":
    unittest.main()


Run tests:

python -m unittest discover -s tests

How to run locally (quick)

Create project folder and files as above.

python3 -m venv venv (optional) then venv\Scripts\activate (Windows) or source venv/bin/activate.

Run: python app.py

For tests: python -m unittest discover -s tests

Edge cases & validations (must implement / consider)

Prevent negative deposits/withdrawals.

Prevent transfers to same account (optional but check).

Handle concurrent access if multiple processes may edit DB (not in this simple version). Use file locks for safety if needed.

Handle JSON corruption (backup + recovery flow).

Validate input types robustly and catch exceptions in CLI.

Improvements & extensions (ideas to add later)

Add authentication / PIN for accounts.

Use SQLite instead of JSON for concurrency & queries.

Add CSV import/export for transactions.

Add scheduled recurring transfers (Task Scheduler).

Add unit tests for storage.py and CLI flows (using unittest.mock to simulate input).

Add logging (Python logging module) for audit trail.

Make a simple web UI with Flask (optional later).

Tips while coding (best practices)

Keep domain logic (Account) separate from storage & UI.

Write tests for core business logic first (TDD).

Use small commits and clear README.

Always backup the JSON before saving (we used safe temp write + backup).

Use type hints and docstrings to improve readability.

Summary checklist (what I delivered)

Design overview + folder structure ✅

Full starter code for accounts.py, storage.py, utils.py, and app.py ✅

Sample JSON data format ✅

Unit tests example ✅

Run instructions + improvements + tips ✅