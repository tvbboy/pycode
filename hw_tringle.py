#find the area of a triangle whose three sides are given
a,b,c=input("请输入三角形三条边：").split("-")
a=int(a)
b=int(b)
c=int(c)
s=(a+b+c)/2.0;
area=(s*(s-a)*(s-b)*(s-c))**0.5;
print("三角形的面积是:",area)
