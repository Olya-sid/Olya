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
