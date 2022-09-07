# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:05
# @Author : 程序猿阿辉
# @File : 15_列表高级
# @Project : Python_Spider

# 列表list    用法:name_list = ['name1','name2']

# append    追加      在列表最后添加一个对象/数据
food_list = ['铁锅炖大鹅','酸菜五花肉']
print(food_list)
# 在列表food_list最后追加一个对象
food_list.append('小鸡炖蘑菇')
print(food_list)


# insert    插入      在列表指定位置（索引）添加对象
char_list = ['a','c','d']
print(char_list)
# 在列表char_list列表索引为1的位置添加对象'b'
# insert(self,index,)
# index的值是索引
char_list.insert(1,'b')
print(char_list)


#extend     拼接      将列表中元素逐一添加到另一个列表中
# 相当于多次调用append方法
num_list = [1,2,3]
num1_list = [4,5,6]

num_list.extend(num1_list)
print(num_list)

