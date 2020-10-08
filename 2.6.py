def Fibonacci(s):
    a = [1, 1]
    for i in range(2, s + 1):
        a.append(i)
        a[i] = a[i - 1] + a[i - 2]
    return a[s]



s = int(input())
print(Fibonacci(s))
