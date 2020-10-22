def toCamelCase(a):
    b = []
    c = ''
    for i in a:
        b.append(i)
    for i in range(len(b)):
        if b[i - 1] == '_':
            b[i] = b[i].upper()
            b[i - 1] = ''
        c += b[i - 1]
    return c[1:] + b[-1]


a = input()
print(toCamelCase(a))

def toSnakeCase(a):
    b = []
    c = ''
    for i in a:
        b.append(i)
    for i in range(len(b)):
        if b[i].isupper():
            b[i] = b[i].lower()
            b[i - 1] += '_'
        c += b[i - 1]
    return c[1:] + b[-1]


a = input()
print(toSnakeCase(a))
