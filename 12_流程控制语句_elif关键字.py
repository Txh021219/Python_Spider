# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 15:06
# @Author : 程序猿阿辉
# @File : 12_流程控制语句_elif
# @Project : Python_Spider

# elif关键字用于多条件判断

score = int(input('你的成绩'))

if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('合格')
else:
    print('不及格')