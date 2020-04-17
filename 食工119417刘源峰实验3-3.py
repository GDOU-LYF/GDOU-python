def year_day(year,month,day):
    day1=[0,31,28,31,30,31,30,31,31,30,31,30,31]#先定义普通年份的每个月天数的列表
    sum=0#先设定返回值为0
    if (year%4==0 and year%100!=0 )or year%400==0:#判断是否为闰年
        # if  month>=2:#如果输入的月份大于2月,那么改变2月的基础天数为29
        day1[2]+=1#与day1[2]=day1[2]+1一样
    for i in range(month):#循环
        sum+=day1[i]#将每个月(不含本月)基础天数加起来
    sum+=day#将本月的天数加起来
    return sum#返回year年的第几天
year= int(input('请输入日期：年 = '))
month = int(input('请输入日期：月 = '))
day = int(input('请输入日期：日 = '))
ret=year_day(year,month,day)
#print(ret)
print("\n您输入的日期是:{}年{}月{}日".format(year,month,day))
print("\n{}年{}月{}日是该年中的第{}天".format(year,month,day,ret))
