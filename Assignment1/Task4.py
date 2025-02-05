# Task 4
def form_dict(*args):
    result_dict = {}
    for arg in args:
        result_dict[arg] = type(arg)
    return result_dict

# Demonstration
print(form_dict(3.5, 1, "text", ("more", "text")))