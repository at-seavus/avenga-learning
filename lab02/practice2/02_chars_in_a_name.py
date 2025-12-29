print("Enter someones name and we will calculate the number of letters from each entry and print back reversed name")

name = input("Enter a name: ")
lastname = input("Enter a lastname: ")

print("Name you entered has ",len(name), "characters")
print("Lastname you entered has ",len(lastname), "characters")

reversed_name=""
reversed_lastname=""

for num in range(len(name)):
    reversed_name = reversed_name + name[-1-num]

for num in range(len(lastname)):
    reversed_lastname = reversed_lastname + lastname[-1-num]

print("Result: ",reversed_lastname,reversed_name)
