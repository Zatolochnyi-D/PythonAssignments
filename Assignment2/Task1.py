# Task 1
from random import randint as r
def generate_random_list(length):
    return [r(0, 100) for x in range(length)]

# Demonstration
print(generate_random_list(5)) # Expected: [N, N, N, N, N], where N - random integer in range [0; 100]