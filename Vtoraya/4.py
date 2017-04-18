import math
m = []
x1 = int(input("Введите координаты X первой точки: "))
y1 = int(input("Введите координаты Y первой точки: "))
x2 = int(input("Введите координаты X второй точки: "))
y2 = int(input("Введите координаты Y второй точки: "))
A = math.sqrt(x1**2+y1**2)
B = math.sqrt(x2**2+y2**2)
m.append(A)
m.append(B)
print(min(m))
