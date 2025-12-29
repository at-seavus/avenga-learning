

print("Enter a number of points you got on your test: ")

points = int(input())

while True:
    if points <= 100 and points >=0:
        if points > 90:
            print("You got an A")
            break
        if points > 80:
            print("You got a B")
            break
        if points > 70:
            print("You got a C")
            break
        if points > 60:
            print("You got a D")
            break
        else:
            print("You got an F")
            break
    else:
        print("Wrong number of points entered... Points must be between 0 and 100")