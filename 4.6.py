def bugger(a):
    k = 0
    while a > 9:
        p = 1
        n = a
        while n:
            p *= n % 10
            n //= 10
        k += 1
        a = p
    return k


a = int(input())
print(bugger(a))
