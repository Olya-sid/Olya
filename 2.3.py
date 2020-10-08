def isAvgWhole(a):
    k = 0
    s = 0
    for i in a:
        s += int(i)
        k += 1
    r = s % k
    if r == 0:
        return True
    else:
        return False


s = input()
a = s.split(' ')
print(isAvgWhole(a))
