#判断素数
for i in range(3,20+1):
    flag=1
    for j in range(2,int(i**0.5)+1): #i**0.5= sqrt(i)
        if(i%j==0):
            flag=0
            break
    if flag:
        print(i,end=" ")
    else:
        pass
        #print("{}不是素数".format(i))