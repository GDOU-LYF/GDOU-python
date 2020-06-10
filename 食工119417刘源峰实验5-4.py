avr=0
a={}
N=10
for i in range(N):
    name=input("姓名:")
    cs=eval(input("成绩:"))
    a[name]=cs
    avr+=cs
avr/=N
for i in a.keys():
    if a.get(i)>=avr:
        print("{}".format(i))