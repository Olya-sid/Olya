a = []
n = int(input())
k = 0
s = 0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i] < a[i-1]:
        k += 1
    elif a[i] > a[i-1]:
        s += 1
print(k + s)
