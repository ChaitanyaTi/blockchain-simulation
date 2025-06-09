import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def next_block(last_block, data):
    index = last_block.index + 1
    timestamp = datetime.datetime.now()
    return Block(index, timestamp, data, last_block.hash)

# Create blockchain with 3 blocks
blockchain = [create_genesis_block()]
blockchain.append(next_block(blockchain[-1], "Block 1 Data"))
blockchain.append(next_block(blockchain[-1], "Block 2 Data"))

# Display original blockchain
print("🔗 Original Blockchain:")
for block in blockchain:
    print(f"Block {block.index} - Hash: {block.hash}")

# Tamper with Block 1
print("\n⚠️ Tampering Block 1...")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Show impact
print("\n🚨 Blockchain After Tampering:")
for block in blockchain:
    print(f"Block {block.index} - Hash: {block.hash}")
