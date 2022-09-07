# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:33
# @Author : 程序猿阿辉
# @File : 18_列表高级_删除
# @Project : Python_Spider


a_list = [1,2,3,4,5]

print(a_list)
# del根据下标index删除列表中数据
# 用法：del name_list[index]
del a_list[3]
print(a_list)


b_list = [1,2,3,4,5]
print(b_list)
# pop删除列表中最后一个数据
b_list.pop()
print(b_list)


# remove    根据元素的值删除元素
c_list = [1,2,3,4,5]
print(c_list)

# 根据元素的值进行删除
c_list.remove(4)
print(c_list)