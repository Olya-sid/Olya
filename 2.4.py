def cumulativeSum(a):
    k = 0
    for i in range(len(a)):
        k += int(a[i])
        a[i] = k
    return a


s = input()
a = s.split(' ')
print(cumulativeSum(a))
