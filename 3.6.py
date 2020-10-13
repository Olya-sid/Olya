def same(a, b):
    k = []
    p = []
    for i in range(len(a)):
        if a[i] != a[i - 1]:
            k.append(a[i])
    for j in range(len(b)):
        if b[j] != b[j - 1]:
            p.append(b[j])
    if len(k) == len(p):
        return True
    else:
        return False


s = input()
m = input()
a = s.split(' ')
b = m.split(' ')
print(same(a, b))
