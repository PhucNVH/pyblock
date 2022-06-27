class Wallet:
    def __init__(self, address, initial_balance=1000, random_seed=None):
        self.address = address
        self.initial_balance = initial_balance

    def public_key(self):
        return self.address

    def private_key(self):
        return self.address

    def sign(self, random_seed, transaction):
        if self.random_seed == random_seed:
            return True
        return False

    def __str__(self):
        return self.address
