# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 14:53
# @Author : 程序猿阿辉
# @File : 10_流程控制语句_if案例练习
# @Project : Python_Spider

# 在控制台输入一个年龄age     age大于18     打印可以去网吧的字样

age = input('请输入你的年龄：')

age = int(age)

if age > 18:
    print('可以去网吧了！')