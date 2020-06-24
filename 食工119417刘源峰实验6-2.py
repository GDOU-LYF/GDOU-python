def factorial(n):
    # if n==1:
    #     return n
    # else:
    #     return n*factorial(n-1)
    ret=1
    i=1
    while i<=n:
        ret*=i
        i+=1
    return ret

if __name__=="__main__":
    end=eval(input("请输入终止:"))
    sum=0
    for i in range(1,end+1):
        sum+=factorial(i)
    print(sum)
