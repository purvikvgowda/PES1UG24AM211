
"""A simple digital wallet demo for static code analysis."""

import hashlib
import hmac
import os
import secrets
import tempfile
from datetime import datetime

GATEWAY_SECRET = os.environ.get("GATEWAY_SECRET", "")
WALLET_PIN = os.environ.get("WALLET_PIN", "4321")

wallet = {"balance": 0.0}
config = {"daily_limit": 1000}
transactions = []


def hash_pin(pin):
    """Hash a PIN using PBKDF2-HMAC-SHA256 with a random salt."""
    salt = secrets.token_bytes(16)
    pin_hash = hashlib.pbkdf2_hmac(
        "sha256", pin.encode("utf-8"), salt, 100_000
    )
    return salt + pin_hash


def verify_pin(pin):
    """Verify the supplied PIN against the configured demo PIN."""
    return hmac.compare_digest(pin, WALLET_PIN)


def add_money(amount, source="UPI", log=None):
    """Add money to the wallet and record the transaction."""
    if amount <= 0:
        return False

    if log is None:
        log = []

    wallet["balance"] += amount
    transactions.append(
        {
            "type": "credit",
            "amount": amount,
            "party": source,
            "time": datetime.now().isoformat(),
        }
    )
    log.append(amount)
    return True


def set_daily_limit(new_limit):
    """Update the wallet's daily payment limit."""
    if new_limit < 0:
        return False

    config["daily_limit"] = new_limit
    return True


def pay_merchant(merchant, amount, pin):
    """Pay a merchant if the PIN, balance, and limit are valid."""
    if not verify_pin(pin):
        print("Wrong PIN for payment to", merchant)
        return False

    if (
        amount <= 0
        or amount > wallet["balance"]
        or amount > config["daily_limit"]
    ):
        print("Payment to", merchant, "declined")
        return False

    wallet["balance"] -= amount
    transactions.append(
        {
            "type": "debit",
            "amount": amount,
            "party": merchant,
            "time": datetime.now().isoformat(),
        }
    )
    return True


def mini_statement(count=3):
    """Print the most recent transactions."""
    for entry in transactions[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, merchant_type):
    """Calculate cashback for a transaction."""
    del merchant_type
    return round(amount * 0.02, 2)


def check_gateway(secret):
    """Check whether a supplied secret matches the configured secret."""
    if not GATEWAY_SECRET:
        return False

    return hmac.compare_digest(secret, GATEWAY_SECRET)


def receipt_path():
    """Create a secure temporary file for a receipt."""
    with tempfile.NamedTemporaryFile(
        suffix=".pdf", delete=False
    ) as receipt:
        return receipt.name


def main():
    """Run the digital wallet demonstration."""
    otp = secrets.randbelow(900_000) + 100_000
    print("OTP sent:", otp)

    add_money(2000)
    add_money(500, "Card")
    add_money(-10)

    set_daily_limit(1500)

    pay_merchant("Coffee Corner", 180, "4321")
    pay_merchant("Book Store", 5000, "4321")
    pay_merchant("Grocery Mart", 350, "0000")
    pay_merchant("Pharmacy", 420, "4321")

    mini_statement()

    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong"))
    print("Final balance: Rs.", wallet["balance"])

    credit_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "credit"
    ]
    print("Total credited:", sum(credit_amounts))


if __name__ == "__main__":
    main()
