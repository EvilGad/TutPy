s = str(input("s="))
s1 = ''
s2 = ''
s3 = ''
m = int
i = 0
z = s.strip()
l = len(z)
while z[i] != ' ':
    s1 = s1 + z[i]
    i = i+1
s1 = s1.strip()
m = z.rindex(' ', 0, l)
j = m
while j<l:
    s2 = s2 + z[j]
    j = j+1
s2 = s2.strip()
for k in range(i, m):
    s3 = s3 + z[k]
s3 = s3.strip()
print(z)
print(s2+' '+s3+' '+s1)