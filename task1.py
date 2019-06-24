a = int(input("Put your number: "))
if a in range(1, 20):
    i = 0
    while i < a:
        print(i**2)
        i += 1
else:
    print("Your number does not fit")
