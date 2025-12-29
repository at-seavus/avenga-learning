print("Enter a year below and I will tell you if it's a leap year...")

year = int(input())


if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print("This is a leap year")
else:
    print("This is NOT a leap year")