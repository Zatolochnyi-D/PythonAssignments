# Task 1
import json

def get_longes_value():
    with open("Resources/task1.json", "r") as f:
        dct: dict = json.load(f)
    result = ""
    for value in dct.values():
        if len(result) < len(value):
            result = value
    return result

# Demonstration
print(get_longes_value()) # Expected: thelongestanswer


# Task 2
def write_py_file():
    f = open("Resources/li.py", "w")
    f.write("li_1 = [1, 2]\n")
    f.close()
    with open("Resources/li.py", "a+") as f:
        f.write("li_2 = ['red', 'green']\n")
        f.seek(0)                             # Put file cursor to the beggining of the file, so readlines() method can read file.
        for line in f.readlines():
            print(line.strip())               # Print line without \n at the end.
            
# Demonstration
write_py_file() # Expected:
                # li_1 = [1, 2]
                # li_2 = ['red', 'green']


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



# Task 4
def write_numbers_then_read_numbers_and_find_min_and_write_to_another_file():
    given = input("Enter numbers: ")
    with open("Resources/task4_1.txt", "w") as f1:            # Create list of ints from input with list comprehension, turn it into a tuple and
        f1.write(str(tuple([int(x) for x in given.split()]))) # and then turn it into a string and then write it to task4_1.txt
    with open("Resources/task4_1.txt", "r") as f1:
        with open("Resources/task4_2.txt", "w") as f2:        # Read from task4_1.txt string, eval it into a tuple, find min value, turn it into a string
            f2.write(str(min(eval(f1.read()))))               # and write it to task4_2.txt

# Demonstration
write_numbers_then_read_numbers_and_find_min_and_write_to_another_file()


# Task 5
from pathlib import Path

def play_with_pathlib():
    print("Creating folder...")
    root = Path('Resources/test_dir')
    root.mkdir()
    print("Creating file...")
    file = Path('Resources/test_dir/test_file.txt')
    with file.open("+w") as f:
        print('Added "Python" to file')
        f.write("Python")
        f.seek(0)
        print(f.read())
    print("Removed file")
    file.unlink()
    print("Removed folder")
    root.rmdir()
        
# Demonstration
play_with_pathlib() # Expected:
                    # Creating folder...
                    # Creating file...
                    # Added "Python" to file
                    # Python
                    # Removed file
                    # Removed folder