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