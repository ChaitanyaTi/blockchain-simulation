import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        print(f"⛏️ Mining block with difficulty {difficulty}...")
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"✅ Block mined: {self.hash}")
        print(f"🔢 Nonce: {self.nonce} | ⏱️ Time taken: {end_time - start_time:.4f} seconds")

# Create and mine a block
mined_block = Block(0, str(datetime.now()), "Mining Simulation Block", "0")
mined_block.mine_block(difficulty=4)
