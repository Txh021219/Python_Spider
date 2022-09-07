# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 14:41
# @Author : 程序猿阿辉
# @File : 09_流程控制语句_if关键字
# @Project : Python_Spider

# if关键字的语句结构
# if    判断条件 :
#       代码（如果判断条件为ture时，执行if里面的内容

age = input('你现在几岁？')
# 转换格式
age = int(age)
# python强调缩进，四个空格或一个tab
# 如果年龄大于18，则可以考驾照
if age > 18:
    print("考驾照去吧！")

