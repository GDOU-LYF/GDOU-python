# 已知变量k的值，求k以内（包括k）各个数的阶乘之和：
# r = 1! + 2! + …… + k!
# 并将结果存放于变量r中。


import sys
if len(sys.argv) < 2:
    k = 5  # 设置k的默认值为5
else:
    k = int(sys.argv[1])

#------------------------------------
# 1、请在两条虚线之间编写代码，否则零分；
# 2、不得使用input()或print()，否则零分；
# 3、变量k的值已经给定，无需另外重新赋值，直接对k编写程序；
# 4、将结果存放在变量r中。
def multiple(x):
    if x==1:
        return 1
    else:
        return x*multiple(x-1)
r=0
for i in range(1,k+1):
    r+=multiple(i)

#------------------------------------
print(r)  # 输出结果r
