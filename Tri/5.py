import math
k = int(input("Введите k: "))
Y = int
if k != 0:
    for n in range(1,k+1):
        Y = ((math.pow((-1),2*n))*(((n**2)-9)**2))/math.factorial(3*n)
print(Y)