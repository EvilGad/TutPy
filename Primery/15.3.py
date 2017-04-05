import math
m = int(input())
y = int(input())
N = ((m**5) + 2.8*m +0.355)/ (math.cos(2*y) + 3.6)
print(N)