a = int(input("Put your number: "))
if ((a <= 20) and (a >= 1)):
    i = 0
    while i < a:
        print(i**2)
        i += 1
else:
    print("Your number does not fit")
