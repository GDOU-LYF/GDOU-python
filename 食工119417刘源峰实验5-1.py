a=[4,6,8,9,12,15,20,34]
x=eval(input("请输入插入的数据:"))
a.append(x)

for i in range(len(a)-1,0,-1):
    flag=0
    for j in range(0,i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            flag=1
    if  flag==0:
        break
for i in a:
    print("{} ".format(i),end="")
print("")