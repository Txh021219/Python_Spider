# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:41
# @Author : 程序猿阿辉
# @File : 19_元组高级
# @Project : Python_Spider

# 元组与列表的区别：元组中的数据不可修改，列表则可以修改

a_tuple = (1,2,3,4)
print(a_tuple)

# 该方法错误，元组不能修改组中数据
# a_tuple[3] = 10

# 列表元素则可以被修改
# a_list = [1,2,3,4]
# a_list[3] = 10
# print(a_list[3])


# 当元组中只有一个元素    类型为int整型
# 定义只有一个元素的元组，需要在唯一的元素后加逗号,
b_tuple = (10086)
print(type(b_tuple))