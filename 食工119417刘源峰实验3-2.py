x=float(eval(input("请输入x:")))
if x<0 and x!=-3:
    ret=x**2+x-6
elif 0<=x<10 and x!=2 and x!=3:
    ret=x**2-5*x+6
else:
    ret=x**2-x-1
print(ret)
