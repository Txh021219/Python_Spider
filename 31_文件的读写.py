# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 18:08
# @Author : 程序猿阿辉
# @File : 31_文件的读写
# @Project : Python_Spider


# 写数据
# write方法
# 'a'访问方式，在尾部追加已存在文件内容
fp = open('test.txt','a')

fp.write('hello python world!\n' * 5)

fp.close()


# 读数据       前提是数据存在
# read方法
fp = open('test.txt','r')
# 默认情况下read是每个字节读取  效率较低
cotent = fp.read()
print(type(cotent))
# str类型
print(cotent)


# readline方法     只读取一行
# content = fp.readline()
# print(content)

# readlines方法       按行读取        会将所有数据都读取，并以列表形式返回每一行
# 列表的元素为每行的数据
# content = fp.readlines()
# print(content)



