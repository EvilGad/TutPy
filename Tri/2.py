import math
n = int(input("n="))
lst=[]
for i in range(2, n+1):
    for j in lst:
        if j > int((math.sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print(lst)