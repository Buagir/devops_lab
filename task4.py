a = int(input('Input your number: '))
if a in range(1, 99):
    b = bin(a)[2:]
    s = len(b)
    i = 0
    k = " "
    for i in range(1, a):
        print(str(i).rjust(s) + k + oct(i)[2:].rjust(s) + k + hex(i)[2:].rjust(s) + k + bin(i)[2:].rjust(s))
        i += 1
else:
    exit
