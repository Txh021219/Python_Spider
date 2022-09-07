# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:58
# @Author : 程序猿阿辉
# @File : 21_字典高级_查询
# @Project : Python_Spider


# 定义字典person
person = {'name':'蔡徐坤','age':18}

# 访问person中的name,age值
print(person['name'])
print(person['age'])

# 获取字典中不存在的key值         报错key值error
# print(person['sex'])

# 不可以使用.方式访问字典的数据
# print(person.name)

# 获取字典中数据的另一种方法     get('key')
print(person.get('name'))

# 使用.方法获取字典中不存在的key值        会返回None
print(person.get('sex'))