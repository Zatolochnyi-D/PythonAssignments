# Task 1
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

# Task 2
def combine_dicts(dicts):
    keys = set()                                    # Set to collect distinct keys.
    for dict in dicts:                              # Go through all given dicts.
        for key in dict.keys():                     # Go through keys of each dict.
            keys.add(key)                           # Add key to set (and it's discarded if there is already the same key inside).

    result_dict = {}                                
    for key in keys:                                # Go through all the keys.
        result_dict[key] = []                       # Create list under key in resulting dict.
        for dict in dicts:                          # Go through all gicen dicts.
            try:                                    # Add to created ealrier list value under the same key in each dict.
                result_dict[key].append(dict[key])
            except KeyError:                        # If dict does not have such key, skip.
                continue

    return result_dict

# Demonstration
dicts = [
    {
        "a": "letter",
        "b": "letter",
        "c": "letter",
    },
    {
        "b": "letter",
        "d": "letter",
        "1": "number",
    },
    {
        "c": "letter",
        "1": "number",
        "2": "number",
    },
]
print(combine_dicts(dicts)) # Expected (in any order): {'1': ['number', 'number'], '2': ['number'], 'b': ['letter', 'letter'], 'd': ['letter'], 'c': ['letter', 'letter'], 'a': ['letter']}

# Task 3
def get_active_names(names):
    result_list = []
    for dict in names:                       # Go through all the dicts.
        if dict["status"]:                   # Take dict's name to result list if it's status is True.
            result_list.append(dict["name"])
    return result_list

# Demonstration
names = [
    {
        "status": True,
        "name": "Arthos",
    },
    {
        "status": True,
        "name": "Porthos",
    },
    {
        "status": True,
        "name": "Aramis",
    },
    {
        "status": False,
        "name": "D'Artagnan",
    },
]
print(get_active_names(names)) # Expected: ['Arthos', 'Porthos', 'Aramis']

# Task 4
def form_dict(*args):
    result_dict = {}
    for arg in args:                  # Create new key of given argument and set it's value to type of argument.
        result_dict[arg] = type(arg)
    return result_dict

# Demonstration
print(form_dict(3.5, 1, "text", ("more", "text")))

# Task 5
ua2eng = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "е": "e",
    "є": "ye",
    "ж": "j",
    "з": "z",
    "и": "i",
    "і": "i",
    "ї": "yi",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ь": "'",
    "ю": "yu",
    "я": "ya"
}
eng2ua = {
    "a": "а",
    "b": "б",
    "c": "ц",
    "d": "в",
    "e": "е",
    "f": "ф",
    "g": "ґ",
    "h": "г",
    "i": "і",
    "j": "ж",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "к'ю",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "в",
    "w": "в",
    "x": "кс",
    "y": "й",
    "z": "з",
}

def transliterate(table, string):
    result = ""                                      # String to put transliterated characters in.
    for char in string:                              # Go through each character in provided word.
        transliterated = table[char.lower()]         # Get corresponding transliterated character.
        if char.isupper():                           # Convert transliterated character to upper case, if original character was in upper case.
            transliterated = transliterated.upper()
        result += transliterated                     # Append transliterated character to string.
    return result
        
# Demonstration
print(transliterate(ua2eng, "Паляниця")) # Expected: Palyanicya
print(transliterate(eng2ua, "Program")) # Expected: Проґрам