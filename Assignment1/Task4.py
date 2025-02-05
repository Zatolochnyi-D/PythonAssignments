# Program
def form_dict(*args):
    result_dict = {}
    for arg in args:                  # Create new key of given argument and set it's value to type of argument.
        result_dict[arg] = type(arg)
    return result_dict

# Demonstration
print(form_dict(3.5, 1, "text", ("more", "text")))