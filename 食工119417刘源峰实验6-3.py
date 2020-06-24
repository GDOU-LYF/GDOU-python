def factorial(n):
    # if n==1:
    #     return n
    # else:
    #     return n*factorial(n-1)
    ret=1
    i=1
    if n!=int(n):
        n=int(n)
    while i<=n:
        ret*=i
        i+=1
    return ret

def s(x,n):
    return x+1/factorial(n)

def f(x,n):
    return s(x,n)/(s(x+1.75,n)+s(x,n+5))

if __name__=="__main__":
    x,n=eval(input("请输入x,n;用,分割:"))
    print("{:.4}".format(f(x,n)))