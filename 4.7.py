def toStarShorthand(a):
    b = []
    k = 0
    c = ''
    a += '0'
    for i in a:
        b.append(i)
    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            k += 1
            b[i - 1] = ''
        else:
            if k > 0:
                b[i - 1] = b[i - 1] + '*' + str(k + 1)
            k = 0
        c += b[i - 1]
    return c


a = input()
print(toStarShorthand(a))
