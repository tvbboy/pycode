#要求：小王希望用电脑记录他每天掌握的英文单词。请设计程序和相应的数据结构，使小王能记录新学的英文单词和其中文翻译，并能很方便地实现中英文互查。

_______________
while True:
    print("请选择功能：\n1: 输入\n2：查找\n3：退出")
    c=input()
    if c=="1":
        word=input("请输入英文单词（按回车结束）：")
        if len(word)==0:
            break;
        meaning=input("请输入中文翻译：")
        dic[word]=meaning
        print("该单词已添加到字典库。")

    elif __________:
        word=input("请输入要查询的英文单词（按回车结束）：")
        if len(word)==0:
            break;
        if word in dic:
            print("_____的中文翻译是_______"%(word,dic[word]))
        else:
            print("字典库中未找到这个单词")

    elif c=="3":
        _________________
    else:
        print("输入有误！")