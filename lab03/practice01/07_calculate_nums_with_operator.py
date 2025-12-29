print("Enter a number, an operator and another number")

num1 = float(input("Enter first number here: "))
operator = input("Enter your operator (+,-,*,/): ")
num2 = float(input("Enter second number here: "))

if operator not in ['+','-','*','/']:
    print("Operator is wrong, try again")
    exit(1)

print("Result is: ",eval(f"({num1} {operator} {num2})"))