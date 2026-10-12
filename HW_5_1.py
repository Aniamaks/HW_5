import string
import keyword

variable_name = input("Enter a variable name: ")

is_valid = True

if variable_name == "":
    is_valid = False

elif variable_name[0].isdigit():
    is_valid = False

elif variable_name.strip("_") == "" and len(variable_name) > 1:
    is_valid = False

elif variable_name in keyword.kwlist:
    is_valid = False

for char in variable_name:
    if char.isupper() or char == " " or (char in string.punctuation and char != "_"):
        is_valid = False

print(is_valid)