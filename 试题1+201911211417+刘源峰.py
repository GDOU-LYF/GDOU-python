# 已知有一个列表aList，请编写代码，
# 求aList中所有偶数元素的总和，并将结果存放于变量total中。

import sys
if len(sys.argv) < 2:
    aList = [4,6,8,9,12,15,20,34]  # 已设置aList的默认值
else:
    aList = eval(sys.argv[1])



#------------------------------------
# 1、请在两条虚线之间编写代码，否则零分；
# 2、不得使用input()或print()，否则零分；
# 3、列表aList已经给定，无需另外重新给定，直接对列表aList编写程序；
# 4、将结果存放在变量total中。
total=0
for x in aList:
    if x%2==0:
        total+=x



#------------------------------------
print(total)  # 输出结果total

