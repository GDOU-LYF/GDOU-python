#输出 公母小鸡数目
#依据题目意思 5a+3b+(1/3)c=100
#应该用3重循环,改进:
M=100
print("鸡翁\t鸡母\t鸡雏")
# for i in range(0,21):#方法一
#     for j in range(0,33):
#         for k in range(0,300):
#             if i*15+j*9+k==300 and i+j+k==100:
#                 print("{}\t{}\t{}".format(i,j,k))

for a in range(0,M+1):#优化
    for b in range(0,M+1):
        c=M-a-b
        if 15*a+9*b+c==M*3:
            print("{}\t{}\t{}".format(a,b,c))