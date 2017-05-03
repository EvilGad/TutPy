s = str(input("s="))
k = s.rindex(' ', 0,len(s))
print(s[:(k)] + s[k+1:])