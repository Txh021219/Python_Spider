# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 15:59
# @Author : 程序猿阿辉
# @File : 40_urllib_get请求的urlencode方法
# @Project : Python_Spider


# urlencode应用场景     多个参数时

# https://www.baidu.com/s?wd=周杰伦&sex=男

# import urllib.parse
#
#
# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)
# #parse.urlencode会把字典中每个键值对拼接起来，并且在每个键值对之间加&

# 获取网页源码https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

import urllib.request
import urllib.parse


base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

# 将字典中的每个键值对转换为unicode格式
new_data = urllib.parse.urlencode(data)
# print(new_data)

# 请求资源路径
url = base_url + new_data

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据
# print(type(content))
print(content)