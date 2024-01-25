import os
def getallfiles(dir):
#"""使用listdir循环遍历"""   
    if not os.path.isdir(dir): #如果不是目录
        print("file:",dir)
        return   
    print("folder:",dir)
    dirlist = os.listdir(dir)
    for dirret in dirlist:
        fullname = dir + "\\" + dirret
        getallfiles(fullname)
dir=r"D:\test"
getallfiles(dir)