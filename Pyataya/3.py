import random
m = 5
n = 5
i = 0
j = 0
s = 0
a = [[random.randint(1, 9) for i in range(n)] for j in range(m)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if i<j:
            s = s + a[i][j]
        print(a[i][j], end=' ')
    print()
print("Сумма элементов выше левой диагонали = ",s)
