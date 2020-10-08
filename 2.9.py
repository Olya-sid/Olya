def isPreffix(a, b):
    k = 0
    for i in range(len(b) - 1):
        if a[i] == b[i]:
            k += 0
        else:
            k += 1
    if k == 0:
        return True
    else:
        return False
def isSuffix(a, b):
    k = 0
    for i in range(1, len(b) - 1):
        if a[-i] == b[-i]:
            k += 0
        else:
            k += 1
    if k == 0:
        return True
    else:
        return False

a = input()
b = input()
print(isPreffix(a, b))
print(isSuffix(a, b))
