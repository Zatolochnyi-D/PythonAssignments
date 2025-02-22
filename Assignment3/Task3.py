# Task 3
from random import randint as r
import pickle

def write_randoms():
    lst = [r(-100, 100) for x in range(5)]
    print(f"generated list: {lst}")
    with open("Resources/task3.bin", "wb") as f:
        pickle.dump(lst, f)

def read_and_sum_randoms():
    with open("Resources/task3.bin", "rb") as f:
        lst = pickle.load(f)
    with open("Resources/task3.txt", "w") as f:
        f.write(str(sum([x for x in lst if 0 <= x <= 10])))

# Demonstration
write_randoms()         # Expected: [N, N, N, N, N] where N - random number in range [-100, 100]
read_and_sum_randoms()  # Expected: will be written to task3.txt
