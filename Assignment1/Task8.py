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