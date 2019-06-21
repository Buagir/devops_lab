a = int(input('Input your number: '))
if a <= 99 and a >= 1:
    b = bin(a)[2:]
    s = len(b)
    i = 0
    for i in range(0, a):
        print(str(i).rjust(s) + oct(i)[2:].rjust(s) + hex(i)[2:].rjust(s) + bin(i)[2:].rjust(s))
        i += 1
else:
    exit
