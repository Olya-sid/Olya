def isValidHexCode(a):
    k = 0
    B = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
    if a[0] == '#' and len(a) < 8:
        for i in range(1, len(a)):
            if not a[i] in B:
                k += 1
        if k == 0:
            return True
        else:
            return False
    else:
        return False


a = input()
print(isValidHexCode(a))
