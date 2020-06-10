a="Python"
# b=list(a)
b=""
for i in range(1,len(a)+1):
    # b[i-1]=a[-i]
    b+=a[-i]
a=b

for i in a:
    print("{}".format(i),end="")
print("")