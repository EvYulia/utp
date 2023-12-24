a=[1,2,212,7,33,214,5]
amax=a[1]
for i in range(len(a)):
    if amax<=a[i]:
        amax=a[i]
print(amax)
