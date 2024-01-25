#这是使用非split和list的做法
email=input("please input a email:")
email_reverse=email[::-1]
dot_postion=email_reverse.find('.')
top_domain=email_reverse[:dot_postion]
print("top domain:",top_domain[::-1])