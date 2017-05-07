import random
n = int(input("Введите N: "))
i = 0
j = 0
s = 0
a = [[random.randint(1, 9) for i in range(n)] for j in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i < n-j-1:
            a[i][j] = 0
        elif i > n-j-1:
            a[i][j] = 2
        else:
            a[i][j] = 1
        print(a[i][j], end=' ')
    print()