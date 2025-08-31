number = int(input("Enter a number: "))

if number == 0:
    print("Number is zero")
elif number > 0:
    if number % 2 == 0:
        print("Number is a positive even number")
    else:
        print("Number is a positive odd number")
else:
    if number % 2 == 0:
        print("Number is a negative even number")
    else:
        print("Number is a negative odd number")
