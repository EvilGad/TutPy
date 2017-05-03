s = str(input("s="))
k = 0
l = len(s)
for j in range(0, l):
    if (s[j] == "(") or (s[j] == ')') or (s[j] == ']') or (s[j] == '['):
        k = k+1
print(k)