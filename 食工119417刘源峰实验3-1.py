a,b,c=eval(input("请输入三角形的三边,用(,)分割:"))
if a+b>c and a+c>b and b+c>a:
    tures=True
else:
    tures=False
if tures:
    string="The triangle being made up of a, b and c is "
    if a==b==c:
        print(string+"equilateral triangle")
    elif a==b or a==c or b==c:
        print(string+"isosceles spherical triangle")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print(string+"right angled triangle")
    else:
        print(string+"ordinary triangle")
else:
    print("No triangle!")