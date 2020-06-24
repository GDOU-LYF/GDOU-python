def isprime(n):
    flag=True
    if n==2 or n==3:
        return flag
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            flag=False
            break
    return flag

if __name__=="__main__":
    start,end=eval(input("请输入起始和终止数,用,分割:"))
    for i in range(start,end+1):
        if isprime(i):
            print(i)
