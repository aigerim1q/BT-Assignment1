import hashlib
import time
def hash(text):
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_tree(transactions)

    def build_tree(self, transactions):
        if len(transactions) == 1:
            return hash(transactions[0])

        new_level = []
        for i in range(0, len(transactions), 2):
            left = transactions[i]
            right = transactions[i + 1] if i + 1 < len(transactions) else left
            new_level.append(hash(left + right))

        return self.build_tree(new_level)
class Block:
    def init(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.merkle_root = MerkleTree(transactions).root
        self.hash = None

        def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.merkle_root}"
        return hash(block_string)
        
class Blockchain:
    def init(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

