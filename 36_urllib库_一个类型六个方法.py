# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 11:08
# @Author : 程序猿阿辉
# @File : 36_urllib库_一个类型六个方法
# @Project : Python_Spider


import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型六个方法
# response是HTTPResponse类型
print(type(response))

# 按照一个个字节去读
# content = response.read()
# print(content)

# 返回n个字节
# content = response.read(n)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 读取多行
# content = response.readlines()
# print(content)

# 返回状态码     如果是200  证明逻辑没错
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# # 获取状态信息
# print(response.getheaders())

# 一个类型  HTTPResponse
# 六个方法  read    readline    readlines   getcode   geturl  getheaders