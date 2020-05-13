#1,3,5,7 组成互不相同的三位数,每行6个
a=['1','3','5','7']
count=0
for i in a:
    for j in a:
        for k in a:
            if i!=j and i!=k and j!=k:
                print(i+j+k,end=',')
                count+=1
                if count==6:
                    count=0
                    print()
