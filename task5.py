b = input().split()
f = map(int, b)
ee = map(int, input().split())
c = set(map(int, input().split()))
u = set(map(int, input().split()))
happ = 0
for i in ee:
    if i in c:
        happ += 1
    elif i in u:
        happ -= 1
print(happ)
exit
