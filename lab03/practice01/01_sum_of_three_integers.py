print("Enter three integers below...")

int1 = int(input("First integer: "))
int2 = int(input("Second integer: "))
int3 = int(input("Third integer: "))

if int1 == int2 or int1 == int3 or int2 == int3:
    print("Result is: 0")
else:
    print("Result is: ", int1+int2+int3)