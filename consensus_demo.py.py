import random
from collections import Counter

pow_validators = {
    'MinerA': random.randint(10, 100),
    'MinerB': random.randint(10, 100),
    'MinerC': random.randint(10, 100)
}
pow_winner = max(pow_validators, key=pow_validators.get)

pos_validators = {
    'StakerA': random.randint(10, 100),
    'StakerB': random.randint(10, 100),
    'StakerC': random.randint(10, 100)
}
pos_winner = max(pos_validators, key=pos_validators.get)

delegates = ['Delegate1', 'Delegate2', 'Delegate3']
voters = [random.choice(delegates) for _ in range(3)]
vote_counts = Counter(voters)
dpos_winner = vote_counts.most_common(1)[0][0]

print("⚙️ PoW Simulation:")
print(f"Validator Powers: {pow_validators}")
print(f"Selected (Most Powerful): {pow_winner}\n")

print("💰 PoS Simulation:")
print(f"Validator Stakes: {pos_validators}")
print(f"Selected (Highest Stake): {pos_winner}\n")

print("🗳️ DPoS Simulation:")
print(f"Votes: {voters}")
print(f"Selected (Most Voted Delegate): {dpos_winner}\n")
