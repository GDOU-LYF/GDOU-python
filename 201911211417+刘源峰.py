# 按要求输出n行n列矩阵

import sys
if len(sys.argv) < 2:
    n = 9  # 设置n的默认值为9
else:
    n = int(sys.argv[1])


#------------------------------------
#（请在两条虚线之间填写代码实现指功能，虚线以外不能改动或编写代码）
#（n的值已经给定，无需另外输入或重新给定，直接按n程序）
# for i in range(1,n+1):
#     for j in range(i,n+i):
#         print("{}\t".format(j),end='')
#     print("")
count=[0,0]
for i in range(1,n+1):
    count[0]+=1
    for j in range(i,n+i):
        count[1]+=1
        if count[0]==count[1]:
            #print("{}\t".format(n),end='')
            print("{:>2} ".format(n),end='')
        else:
            print("{:>2} ".format(j),end='')
    print("")
    count[1]=0
#------------------------------------

