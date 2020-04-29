a,b,c=eval(input("请输入三角形的三边,用(,)分割:"))
if a+b>c and a+c>b and b+c>a:
    tures=True
else:
    tures=False
if tures:
    string="The triangle being made up of a, b and c is "
    if a==b==c:#等边三角形
        print(string+"equilateral triangle")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        #直角三角形
        print(string+"right angled triangle")
    elif a==b or a==c or b==c: #等腰三角形 
            print(string+"isosceles spherical triangle")
    else:#其他三角形
        print(string+"ordinary triangle")
else:#不是三角形
    print("Not a triangle!")