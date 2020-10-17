def isKaprekar(d):
    a = d ** 2
    s = str(a)
    k = 10 ** (len(s) - 1)
    p = 10 ** (len(s) / 2)
    t = False
    if d == 0 or d == 1:
        t = True
    else:
        if len(s) % 2 == 0:
            if a // p + a % p == d:
                t = True
        else:
            for i in range(len(s) // 2):
                if a // k + a % k == d:
                    t = True
                k /= 10
    return t


a = int(input())
print(isKaprekar(a))
