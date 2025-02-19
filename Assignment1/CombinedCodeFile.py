# Taks 1
def find_matches(string1, string2):
    combinations1 = []
    for i in range(1, len(string1)):
        combinations1.append(string1[i-1] + string1[i])    # Read every combination of 2 letters from first string.
    combinations2 = []
    for i in range(1, len(string2)):
        combinations2.append(string2[i-1] + string2[i])    # Read every combination of 2 letters from second string.
    result = []
    for combination in combinations1:                      # Select every combination that is in both combination lists.
        if (combination in combinations2):
            result.append(combination)
    return result

# Demonstration
print(find_matches("akkad", "drakkar")) # Expected: ['ak', 'kk', 'ka']


# Task 2
def len_of_string(string):
    counter = 0
    for letter in string:    # Just increase counter per each iterated symbol.
        counter += 1
    return counter

# Demonstration

print(len_of_string("abcde")) # Expected : 5


# Task 3
def delete_third_elements(list):
    print(list)                    # Print initial list.
    counter = 2 % len(list)        # Start counter that will identify index to remove. Start from 2 (third element). Take remaining
    while (True):                  # if list length is less than 2.
        del list[counter]
        print(list)                # Print list with remove element.
        if (len(list) == 0):       # Stop iteration when list is empty.
            break
        counter += 2               # If list is still not empty, increase counter by 3 - 1 to get next third element. Limit by length of list. How it workds:
        counter %= len(list)       # [1, 2, 3, 1, 2, 3] -> [1, 2, 1, 2, 3]
                                   #        ↑ pointer     pointer ↑     ↑ next needed element

# Demonstration
delete_third_elements([1, 2, 3, 4, 5, 6]) # Expected: [1, 2, 3, 4, 5, 6]
                                          #           [1, 2, 4, 5, 6]
                                          #           [1, 2, 4, 5]
                                          #           [1, 2, 5]
                                          #           [1, 5]
                                          #           [1]
                                          #           []


# Task 4
def replace_symbols(string_list, symbol):
    for string in string_list:              # Stop function if there are words with size less than 3.
        if (len(string) < 3):
            return None
    result_list = []
    for string in string_list:
        result = string[:-2]                # For each word in given list, get substring from 0 to 3-from-end symbol.
        result += symbol * 3                # Add to substring given symbol 3 times.
        result_list.append(result)
    return result_list

# Demonstration
print(replace_symbols(["abcde", "string", "Task4"], "%")) # Expected: ['ab%%%', 'str%%%', 'Ta%%%']


# Task 5
def get_medians(list1, list2):
    return [list1[1], list2[1]]

# Demonstration
print(get_medians([1, 2, 3], [4, 5, 6])) # Expected: [2, 5]]


# Task 6
def sum_strings(list):
    result = 0.0
    for el in list:
        result += float(el)
    return result

# Demonstration
print(sum_strings(["100", "0.5", "-58.5"])) # Expected: 42.0


# Task 7
def get_students_with_good_marks(students):
    result = []
    for student in students:
        if (student["mark"] > 80):               # Select students with mark higher than 80
            result.append(student["last name"])  # Get thair last name. Nothing hard.
    return result

# Demonstration
students = [
    {
        "first name": "Harry",
        "last name": "Potter",
        "mark": 79
    },
    {
        "first name": "Hermione",
        "last name": "Granger",
        "mark": 90
    },
    {
        "first name": "Ron",
        "last name": "Weasley",
        "mark": 70
    },
]
print(get_students_with_good_marks(students)) # Expected: ['Granger']


def get_active_names(names):
    result_list = []
    for dict in names:                       # The same process as in Task 7.
        if dict["status"]:
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