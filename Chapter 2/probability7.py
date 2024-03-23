import numpy as np

def generate(p1):
    # Generates 10000 random zeros and ones where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    count = start = 0
    seq_array = ''.join(seq.astype(str))
    
    while True:
        start = seq_array.find("11111", start) + 1
        if start > 0:
            count += 1
        else:
            return count

def main(p1):
    seq = generate(p1)
    return count(seq)

# Running the simulation 1000 times
results = [main(2/3) for _ in range(30000)]

# Calculating the average of the results
average = np.mean(results)

print(f"Average occurrence: {average}")
