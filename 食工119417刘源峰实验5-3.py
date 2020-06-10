a=[4,6,8,9,12,15,20,34]
for i in range(len(a)):
    if a[i]%2==0:
        a[i]=a[i]**2
    
for i in a:
    print("{} ".format(i),end="")
print("")