# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 16:10
# @Author : 程序猿阿辉
# @File : 23_字典高级_添加
# @Project : Python_Spider


person = {'name':'大司马'}

print(person)

# 给字典添加一个key value
# 使用变量名称['key'] = 数据    如果键值不存在，则变成新键值元素
# 如果键值本身已存在，则会覆盖（修改）原先的值
person['age'] = 33

print(person)


