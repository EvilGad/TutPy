n = 14
m = []
for v in range(1, n+1):
    m.append(float(input()))
print(m)
for i in range(1, 14):
    if i<8:
        for j in range(7-i):
            if m[j]>m[j+1]:
                t=m[j]
                m[j] = m[j+1]
                m[j+1] = t
    else:
        z = 1
        for j in range(7, 14-z):
            if m[j]<m[j+1]:
                t=m[j]
                m[j] = m[j+1]
                m[j+1] = t
            z = z+1
print(m)