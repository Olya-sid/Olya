def d(a, b, c):
    for i in range(b):
        a *= 2
    if a % c == 0:
        return True
    else:
        return False
a = int(input())
b = int(input())
c = int(input())
print(d(a, b, c))
