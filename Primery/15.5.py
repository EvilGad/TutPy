import math
p=4
a=5.5
B = math.fabs(a) + math.sqrt(a+p**2)
X = math.exp(B)
Y = math.pow(math.cos(X),3) + math.fabs(a)
print(X," ", Y ," ", B)

