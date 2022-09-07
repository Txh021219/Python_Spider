# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:20
# @Author : 程序猿阿辉
# @File : 16_列表高级_查找
# @Project : Python_Spider


food_list = ['锅包肉','汆白肉','东北乱炖']

# 判断在控制台输入的数据是否在列表中
# in        判断某元素是否在某个列表中

# food = input('请输入食物的名称：')
#
# if(food in food_list):
#     print('食物在列表中！')
# else:
#     print('没有')

# not in    判断某元素是否不在某个列表中

ball_list = ['篮球','羽毛球']

# 在控制台上输入球类名称   判断是否不在列表中
ball = input('请输入球类名称：')

if ball not in ball_list:
    print('不在')
else:
    print('在')