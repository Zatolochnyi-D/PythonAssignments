# Program
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