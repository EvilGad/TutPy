n = 15
m = []
S = float
for v in range(1, n+1):
    m.append(float(input()))
print(m)
S = float(input("Введите вещественное число из массива S: "))
z = m.index(S)
if z!=((n-1)-z):
    if z<(n-z):
        print("Значение: ",m[n-1],"Индекс: ", n-1)
    else:
        print("Значение: ", m[0],"Индекс: ", '0')
else:
    print("Элемент равноудален от самых дальних значений ")