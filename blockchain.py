import hashlib
from time import time
from block import Block

from transaction import Transaction
from wallet import Wallet


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.initial_difficulty = 2
        self.difficulty = self.initial_difficulty

    def add_block(self, block):
        self.chain.append(block)
        self.current_transactions = []
        if len(self.chain) % 1000 == 0:
            self.difficulty += 1

    def create_block(self, proof, previous_hash=None):
        block = Block(len(self.chain) + 1, time(),
                      self.current_transactions, proof, previous_hash)
        return block

    def new_transaction(self, sender: Wallet, recipient: Wallet, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0" * self.difficulty * self.difficulty_rate
