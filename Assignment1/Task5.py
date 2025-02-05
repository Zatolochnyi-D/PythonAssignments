# Program
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