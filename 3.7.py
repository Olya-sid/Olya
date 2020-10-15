def isKaprekar(d):
    a = d ** 2
    s = str(a)
    h = len(s) - 1
    k = 10
    p = 0
    if d == 0 or d == 1:
        return True
    else:
        for i in range(h):
            if a // k + a % k == d:
                p += 1
            k *= 10
        if p != 0:
            return True
        else:
            return False


a = int(input())
print(isKaprekar(a))
