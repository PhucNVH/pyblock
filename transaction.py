import hashlib

from wallet import Wallet


class Transaction:
    def __init__(self, sender: Wallet, recipient: Wallet, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.inputs = []
        self.outputs = []

    def is_spendable(self, owner):
        return self.recipient == owner

    def __str__(self):
        sha = hashlib.sha256()
        sha.update(str(self.sender) + str(self.recipient) + str(self.amount))
        return sha.hexdigest()
