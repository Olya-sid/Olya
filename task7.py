def x(a):
    k = 0
    for i in range(0, len(a)):
        k += a[i]
    return k + a[-1] + 1
n = int(input())
a = []
for i in range(n):
    a.append(i)
print(x(a))
