def rev():
    a = str(input())
    b = ''.join(reversed(a))
    if a == b:
        print("Your word is polindrom")
    else:
        print("Not polindrom")


rev = rev()
