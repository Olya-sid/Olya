def longestZero(a):
    m = []
    k = 0
    a += '1'
    for i in range(len(a)):
        if a[i] == a[i - 1] and a[i] == '0':
            k += 1
        else:
            if k != 0:
                m.append(k + 1)
            k = 0
    if m == [] and '0' in a:
        n = 1
    elif m == []:
        n = 0
    else:
        n = max(m)
    return '0' * n
