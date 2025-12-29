print("Enter a name and a lastname of some person below...")

name = input("Enter some name here: ")
lastname = input("Enter some lastname here: ")

arr_of_vowels = ['a','e','i','o','u']

if name[2] in arr_of_vowels and lastname[3] in arr_of_vowels:
    print("Both 3rd letter of name and 4th letter of lastname are vowels.")

if name[2] not in arr_of_vowels and lastname[3] not in arr_of_vowels:
    print("Both 3rd letter of name and 4th letter of lastname are consonants.")
else:
    print("This is a mix...")