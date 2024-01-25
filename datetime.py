from datetime import datetime  # 导入必要的日期时间处理包
date_str = "2012-12-1"
year_s, mon_s, day_s = date_str.split('-')
#下面是强转日期时间的语法。参数分别是年，月，日对应的整数
date_var =datetime(int(year_s), int(mon_s), int(day_s))
print(date_str)
print(date_var)