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