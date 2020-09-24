# 1
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
# 2
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
# 3
a = []
n = int(input())
m = 0
k = 0
s = 0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if (a[i] + a[i-1]) > m:
        m = a[i] + a[i-1]
        k = m - a[i-1]
        s = m - a[i]
print(s, k)
