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
    