w, h = input().split()
w = int(w)
k = 0
h = int(h)
canvasArea = w * h
count = int(input())
arr = [[0]*h for i in range(w)]
for i in range(count):
    square = [int(l) for l in input().split()]
for i in range(square[0], square[2]):
    for j in range(square[1], square[3]):
        if arr[i][j] == 0:
            k += 1
arr[i][j] = 1
print(canvasArea - k)
