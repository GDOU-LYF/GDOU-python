# 已知有一个列表aList，请编写代码，
# 求aList中所有元素的平均值，并将结果存放于变量avg中。

import sys
if len(sys.argv) < 2:
    aList = [4,6,8,9,12,15,20,34]  # 已设置aList的默认值
else:
    aList = eval(sys.argv[1])



#------------------------------------
# 1、请在两条虚线之间编写代码，否则零分；
# 2、不得使用input()或print()，否则零分；
# 3、列表aList已经给定，无需另外重新给定，直接对列表aList编写程序；
# 4、将结果存放在变量avg中。
avg=0
for x in aList:
    avg+=x
avg/=len(aList)





#------------------------------------
print(avg)  # 输出结果avg

