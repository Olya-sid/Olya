def isValid(a):
    for i in a:
        if a.isdigit() and len(a) <= 5:
            return True
        else:
            return False


a = input()
print(isValid(a))
