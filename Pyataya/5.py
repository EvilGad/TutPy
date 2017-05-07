import random
n = int(input("Введите N: "))
i = 0
j = 0
s = 0
a = [[random.randint(1, 9) for i in range(n)] for j in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if j+1 == len(a):
            s = s + a[i][j]
        print(a[i][j], end=' ')
    print()
print("Сумма элементов последнего столбца =",s)