def rightTriangle(a, b, c):
    if c ** 2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2:
        return True
    else:
        return False


a = int(input())
b = int(input())
c = int(input())
print(rightTriangle(a, b, c))
