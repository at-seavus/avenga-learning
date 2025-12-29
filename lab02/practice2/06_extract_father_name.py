print("Enter your name in following format:")
print("Name Fathers_name Lastname")

entered_text = input()
print("Now we will extract your fathers name...")
name_arr = entered_text.split(" ")

print(name_arr[1])