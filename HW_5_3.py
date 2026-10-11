import string

my_string = input("Enter a string: ")

for char in string.punctuation:
    my_string = my_string.replace(char, "")

my_string = my_string.title()
my_string = my_string.replace(" ", "")

hashtag = "#" + my_string
print(hashtag[:140])