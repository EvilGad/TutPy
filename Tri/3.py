import math
n = int(input("Введите n: "))
x = float(input("Введите x: "))
j = int
k = float
if math.fabs(x)<1:
    for j in range(1, n+1):
        k = x - (((-1)*n) * ((x*(2*n+1))/(2*n+1)))
else:
    print("Введите x<1")
print (k)