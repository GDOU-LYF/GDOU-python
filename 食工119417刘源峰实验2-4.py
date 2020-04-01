#x,y,z=eval(input("请输入3个数字(用,分割)"))
#根据输出结果进行修改:
x=eval(input("请输入第一个数:"))
y=eval(input("请输入第二个数:"))
z=eval(input("请输入第三个数:"))


#x->y y->z z->x 输出后来数字
#  x->y->z   -->x->z
#  y->z->x   -->y->x
#  z->x      -->z->x
print("交换前x={},y={},z={}".format(x,y,z))
x,y,z=z,x,y
print("交换后x={},y={},z={}".format(x,y,z))