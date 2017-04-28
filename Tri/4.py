n = int(input("Введите n: "))
m = int(input("Введите степень m: "))
s = 0
for i in range(1,n+1):
    k = 1
    for j in range(1, m+1):
        k = k*i
    s = s+k
print (s)