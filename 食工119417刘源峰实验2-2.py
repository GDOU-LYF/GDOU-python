import math
a,b,c=4,5,6
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("边长为{},{},{}的三角形面积为{}".format(a,b,c,area))
