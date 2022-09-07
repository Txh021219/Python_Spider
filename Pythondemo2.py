#list   列表
# 应用场景：当获取到很多个数据时，可以将他们储存到列表中，后直接访问列表
name_list = ["周杰伦","陈奕迅"]
print(type(name_list))
print(name_list)
#tuple  元组
#
name_tuple = (12,19,2002)
print(type(name_tuple))
print(name_tuple)

#dict   字典
#应用场景：scrapy框架使用
#格式 ： 变量名字 = {key:value,key1:value2}
name_dict = {'name':'看星空','age':'20'}
print(type(name_dict))
print(name_dict)

# aa = input()
# print(aa)

# 类型强制转换
# 字符串类型str中出现特殊字符，例如'1.23'，‘a1'等不能转换为整数类型int
# a = '12.34'
# print(float(a))
#布尔类型boolean的值强制转换为str类型，显示的是True和False,转换为整型为0和1
# a = True
# print(str(a))
#str字符串类型转换为布尔类型，空字符串''为False,其他都为True
# a = ''
# print(bool(a))
#列表list,元组turple和字典dict中有数据转换为bool布尔类型则为True,否则为False