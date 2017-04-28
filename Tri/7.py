x = int(input("Введите x: "))
n = int(input("Введите n: "))
s = 3
z = 0
for i in range(1, n+1):
    if (i%2==0):
        z =z - ((x**s)/3**i)
        s = s+2
    else:
        z =z + ((x ** s) / 3 ** i)
        s = s + 2
print('%.3f' % z)
