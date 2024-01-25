#这是使用split+list的做法
email=input("please input a email:")
temp_list=email.split('.')
print("top domain:",temp_list[-1])