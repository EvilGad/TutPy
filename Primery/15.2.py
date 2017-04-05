import math
y = int(input())
j = int(input())
F = (2 * math.sin(0.354*y+1))/(math.log1p(y+2*j))
print(F)