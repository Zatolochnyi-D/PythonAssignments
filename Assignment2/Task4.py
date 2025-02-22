# Task 4
def select_odds_in_range(begin, end):
    return [x for x in range(begin, end + 1) if x % 2 == 1]

# Demonstration
print(select_odds_in_range(3, 9)) # Expected: [3, 5, 7, 9]