# Probability Example

# Dice Probability

total_outcomes = 6

favorable = 1

probability = favorable / total_outcomes

print("Probability of getting 3:")
print(probability)

# Even number 

favorable_even = 3

prob_even = favorable_even / total_outcomes

print("\nProbability of Even Number:")
print(prob_even)

import random
heads =0
tails =0

for i in range(100):
    toss = random.choice(["H", "T"])
    
    if toss == "H":
        heads += 1
    else: 
        tails += 1
        
print("Heads:", heads)
print("Tails:", tails)
