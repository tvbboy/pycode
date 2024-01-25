while True:
    number=int(input("please input the number:"))
    sqrt_root=0
    wuqiongxiao=0.01;
    while(sqrt_root*sqrt_root<=number):
       sqrt_root+=wuqiongxiao
    print("the sqrt of number:{0} is:{1}".format(number,sqrt_root-wuqiongxiao))
