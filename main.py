from blockchain import Blockchain
from wallet import Wallet


def main():
    alice = Wallet(address=None, initial_balance=1000, random_seed=None)
    bob = Wallet(address=None, initial_balance=1000, random_seed=None)
    blockchain = Blockchain()
    blockchain.new_transaction(alice, bob, 100)


if __name__ == "__main__":
    main()
