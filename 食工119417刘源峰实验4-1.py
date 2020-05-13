#1,3,5,7 组成互不相同的三位数,每行6个
a=list("1357")
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

# print(len(a),min(a),max(a))
# print(a.index('3'))
# print(a.count('5'))
# b=[item*2 for item in map(eval,a)]
# print(b)
# c=[i*2 for i in map(eval,a)   if i>2]
# print(c)
# ls=list("ABC")
# ls.insert(1,'z')
# ls.reverse()
# ls.remove('z')
# print(ls)