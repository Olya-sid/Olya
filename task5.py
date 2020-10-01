def x(a, b, c):
    if a + b == c:
        return 'added'
    elif a - b == c or b - a == c:
        return 'substracted'
    elif a * b == c:
        return 'multiplied'
    elif a / b == c or b / a == c:
        return 'devided'
    else:
        return 'none'
c = int(input())
a = int(input())
b = int(input())
print(x(a, b, c))
