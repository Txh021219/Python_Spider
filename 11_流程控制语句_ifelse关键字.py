# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 14:58
# @Author : 程序猿阿辉
# @File : 11_流程控制语句_ifelse关键字
# @Project : Python_Spider

# ifelse的语法
# if    判断条件：
#           判断条件为true时执行的代码
# else:
#           判断条件为false时执行的代码

age = input('你的年龄：')

if int(age) > 18:
    print('去网吧吧！')
else:
    print('好好学习！')