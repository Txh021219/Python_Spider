# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 15:11
# @Author : 程序猿阿辉
# @File : 13_流程控制语句_for循环
# @Project : Python_Spider

# 循环字符串
# range(5)
# range(1,6)
# range(1,10,3)
# 循环一个列表

# 遍历
s = 'China'

# for
# 格式：   for  变量  in  要遍历的数据：
#             方法体
for i in s:
    print(i)

# range 是可迭代对象而不是迭代器；range 对象是不可变的等差序列。
# 语法：range(start, stop ,[step])
# range方法的结果    一个可以遍历的对象
# range(5)  0-4    左闭右开区间[0,5)
for i in range(5):
    print(i)
# range(1,6)
# (起始值,结束值)
# range(1,10,3)
# (起始值，结束值，步长)

# 应用场景      爬取一个列表返回给开发者
# 循环一个列表
a_list = ['Jay','JJ','Eason']

# 遍历列表中的元素
for i in a_list:
    print(i)

# 遍历列表中的下标

# 判断列表元素的个数
print('列表元素个数',len(a_list))
for i in range(len(a_list)):
    print(i)