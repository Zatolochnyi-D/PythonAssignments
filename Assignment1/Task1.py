# Program
def read_date(dates_dict, date):
    try:                         # Try get value under "date" key.
        return dates_dict[date]
    except (KeyError):           # If there is no such key, return empty list.
        return []

# Demonstration
notes = {
    "23.06.1917": ["I Universal"],
    "16.07.1917": ["II Universal"],
    "20.11.1917": ["III Universal"],
    "22.01.1918": ["IV Universal"],
}

print(read_date(notes, "23.06.1917")) # Expected: ['I Universal']
print(read_date(notes, "15.04.1984")) # Expected: []