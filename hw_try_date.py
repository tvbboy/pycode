

# 利用try catch结构，结合日期强转思路，新建hw_try_date.py解决困扰我们许久的格式判断：
# 如何判断一个日期是否合法？
# 要求：提示用户输入年-月-日，用户可以任意输入，将用户输入的字符串作为参数交给自定义函数is_date_valid(date_str)处理，该函数通过返回TRUE和FALSE，来判断输入的字符串是否符合日期格式。
# 主程序中，根据函数的返回值，进行输出，只有正确的日期，才出输出日期合法。
import datetime
def is_date_valid(date_str):
    """
    判断日期格式是否正确
    :param date_str: 日期字符串，格式为YYYY-MM-DD
    :return: True表示日期格式正确，False表示日期格式不正确
    """
    try:
        datelist=datestr.split("-")
        if len(datelist)!=3:
            return False
        x=datetime.datetime(year=int(datelist[0]),month=int(datelist[1]),day=int(datelist[2]))
    except:
        return False
    else:
        return True

datestr=input("请输入日期：年-月-日:")
if is_date_valid(datestr):
    print("日期格式正确")
else:
    print("日期格式不正确")
