# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 16:21
# @Author : 程序猿阿辉
# @File : 25_字典高级_遍历
# @Project : Python_Spider


# 遍历：将数据一个个输出

person = {'name':'鸽鸽','age':'18','sex':'ji'}

# 遍历字典的key
# 遍历字典的value
# 遍历字典的key和value
# 遍历字典的项（元素）

# 遍历字典的key
# 字典.keys()     获取字典中所有的key值    key是个变量名称，可以任意命名
for key in person.keys():
    print(key)

# 遍历字典的value
# 字典.values()     获取字典中所有的value值    value是个变量名称，可以任意命名
for value in person.values():
    print(value)

# 遍历字典的key和value
for key,value in person.items():
    print(key,value)

# 遍历字典的项（元素）
for item in person.items():
    print(item)
    # print(type(item))
# 获取到的每个项被切片成一个元组tuple