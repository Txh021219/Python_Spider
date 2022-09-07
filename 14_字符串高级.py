# _*_ coding : utf-8 _*_
# @Time : 2022/7/30 15:27
# @Author : 程序猿阿辉
# @File : 14_字符串高级
# @Project : Python_Spider

# 获取长度        len             len函数可以获取字符串的长度
# 查找内容        find            查找指定内容在字符串中是否存在，如果存在则返回该内容在字符串中第一次出现的位置(索引值)，不存在返回-1
# 判断     startswith,endswith判断字符串是否以某内容开头/结尾
# 计算出现次数    count           返回str在start和end之间在mystr里出现的次数
# 替换内容       replace         替换字符串中指定的内容，如果指定次数count，则替换不会超过count次
# 切割字符串     split           通过参数的内容切割字符串
# 修改大小写     upper,lower     将字符串变成大、小写
# 空格处理       strip            去空格
# 字符串拼接     join             字符串拼接

# len       lenth长度
s = 'China'
print(len(s))

# find      查找内容
s1 = 'China'
print(s1.find('a'))
# 返回a在s1字符串中索引，找不到则返回-1

# startswith, endswith判断字符串是否以某内容开头 / 结尾
s2 = 'China'
# 是则返回true，否则返回false
print(s2.startswith('c'))# 区别大小写
print(s2.endswith('a'))


# count           返回str在start和end之间在mystr里出现的次数
s3 = 'abbcccc'
print(s3.count('a'),s3.count('b'),s3.count('c'))



# replace     替换字符串中指定的内容，如果指定次数count，则替换不会超过count次
# 用法：   .replace('被替换元素','替换元素')
s4 = 'abbcccc'
print(s4.replace('a','c'))


# 切割字符串     split           通过参数的内容切割字符串
s5 = '1#2#3#4#'
# 按#切割字符串
print(s5.split('#'))
# 切割后变成一个个字符串列表



# 修改大小写     upper,lower     将字符串变成大、小写
s7 = 'China'
print(s7.upper())



# 空格处理       strip            去空格
s8 = '    a    '
print(s8.strip())


# 字符串拼接     join             字符串拼接
s9 = 'a112'
print(s9.join('hello'))
# 在hello字符串中每个元素后插入一个s8字符串