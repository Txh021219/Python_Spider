# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 16:14
# @Author : 程序猿阿辉
# @File : 24_字典高级_删除
# @Project : Python_Spider



# del
#   (1)删除字典中指定的某元素
#   (2)删除整个字典


# clear
#   (3)清空字典 保存字典对象
person = {'name':'大司马','age':'18'}
print(person)

del person['age']
print(person)

# 删除整个字典
# del person

# 清空字典
# person.clear()