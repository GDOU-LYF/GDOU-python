a="Python"
b=",".join(a).split(",")

for i in range(1,len(a)+1):
    b[i-1]=a[-i]
a=b.copy()

for i in a:
    print("{}".format(i),end="")
print("")