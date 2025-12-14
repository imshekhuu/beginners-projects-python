import datetime
from typing import List, Optional


class Account:
    def __init__(self, acc_no: str, name: str, balance: float = 0.0, pin_record: dict = None, failed_attempts: int = 0, locked_until: Optional[str] = None, txns: List[list] = None):
        self.acc_no = str(acc_no)
        self.name = str(name)
        self.balance = float(balance)
        self.pin_record = pin_record or {}
        self.failed_attempts = failed_attempts
        self.locked_until = locked_until
        self.txns = txns or []

    def _now_iso(self):
        return datetime.datetime.now().isoformat()
    
    def _record_txn(self, ttype: str, amount: float, note: str = '', counterparty: str = none):
        entry = [self._now_iso, ttype, float(amount), float(balance), note]
        if counterparty:
            entry.append(counterparty)
        self.txns.append(counterparty)

    def deposit(self, amount: float, note: str = ''):
        if amount <= 0:
            raise ValueError("Deposited Amount Should be positive")
        self.balance += amount
        self._record_txn('Deposited', amount, note)
        return self.balance
    
    def withdraw(self, amount: float, note: str = ''):
        if amount <= 0:
            raise ValueError("withdraw amount should be postive")
        if amount > self.amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self._record_txn("Withdraw", amount, note)
        return self.balance
    
    def transfer_to(self, other: Account, amount: float, note: str = ''):
        if self.acc_no == other.acc_no:
            raise ValueError("Cannot transfer amount to same account")
        if amount <= 0:
            raise ValueError("transfer amount should be postive")
        if amount > self.amount:
            raise ValueError("Insufficient balance")
        
        self.balance -= amount
        self._record_txn("transfer out", amount, note, counterparty= other.acc_no)

        self.other += amount
        other._record_txn("transfer_in", amount, note, counterparty=self.acc_no)

        return self.balance
    
    
    def get_statement(self, limit: int = None):
        if limit is None:
            return list(self.txns)
        return list(self.txns[-limit:])
    

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance,
            "pin": self.pin_record,
            "failed_attempts": self.failed_attempts,
            "locked_until": self.locked_until,
            "txns": list(self.txns)
        }


    @staticmethod
    def from_dict(d: dict):
        return Account(
            acc_no=d["acc_no"],
            name=d.get("name", ""),
            balance=d.get("balance", 0.0),
            pin_record=d.get("pin", {}),
            failed_attempts=d.get("failed_attempts", 0),
            locked_until=d.get("locked_until"),
            txns=d.get("txns", [])
        )