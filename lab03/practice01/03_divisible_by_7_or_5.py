print("Enter a number and I will tell you if it's divisible by 5 or 7...")

your_num = int(input("Your number can be entered here: "))

if your_num % 7 == 0:
    print("Your number is divisible by 7")

if your_num % 5 == 0:
    print("Your number is divisble by 5")

if your_num % 7 != 0 or your_num % 5 != 0:
    print("Your number is not divisilbe by 5 nor 7")