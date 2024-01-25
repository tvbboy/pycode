
# 利用try catch结构，结合强转思路，新建hw_try_negtiveNumber.py解决困扰我们许久的格式判断：
# 如何判断一个输入的内容是负数？
# 要求：提示用户输入负数，用户可以任意输入，将用户输入的字符串作为参数交给自定义函数is_negtive_valid(date_str)处理，该函数通过返回TRUE和FALSE，来判断输入的字符串是否是负数。
# 主程序中，根据函数的返回值，进行输出，是否是负数。
def is_negtive_valid(date_str):
    """
    判断日期格式是否正确
    :param date_str: 日期字符串，格式为YYYY-MM-DD
    :return: True表示日期格式正确，False表示日期格式不正确
    """
    try:
        number=float(date_str)
        if number<0:
            return True # 说明输入的字符串是负数
        else:
            return False
    except:
        return False


datestr=input("请输入一个数：")
if is_negtive_valid(datestr):
    print(datestr,"是一个负数！")
else:
    print(datestr,"不是一个负数！")
