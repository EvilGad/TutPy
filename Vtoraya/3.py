x = float(input("Введите координаты X первой точки: "))
y = float(input("Введите координаты Y первой точки: "))
if (x>=(1-y)):
    if (x>=y):
        if (x<=3-y):
            if (x-y<=1):
                print("Входит")
            else:
                print("Не входит")
