a = []
n = int(input())
m = 189827872637
r = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if abs(a[i] - r) < m:
        m = a[i]
print(m)
