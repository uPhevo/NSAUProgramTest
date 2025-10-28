a = [9,8,6,3,1]
b = 0
for i in range(0,len(a)-1):
    for k in range(i+1,len(a)):
        if a[i] > a[k]:
            b = a[i]
            a[i] = a[k]
            a[k] = b
print(a)
