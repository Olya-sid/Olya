def differenceMaxMin(a):
    ma = int(a[0])
    mi = int(a[0])
    for i in a[1:]:
        if int(i) > int(ma):
            ma = i
        if int(i) < int(mi):
            mi = i
    return int(ma) - int(mi)


s = input()
a = s.split(' ')
print(differenceMaxMin(a))
