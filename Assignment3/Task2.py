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