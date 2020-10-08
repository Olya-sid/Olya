def isStrangePair(a, b):
    if a[0] == b[-1] and a[-1] == b[0]:
        return True
    else:
        return False


a = input()
b = input()
print(isStrangePair(a, b))
