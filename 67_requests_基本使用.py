# _*_ coding : utf-8 _*_
# @Time : 2022/9/18 10:35
# @Author : 程序猿阿辉
# @File : 67_requests_基本使用
# @Project : Python_Spider


#安装requests
# pip install requests

import requests

url = 'https://www.baidu.com'

response = requests.get(url=url)

# 一个类型六个属性
# Response类型
print(type(response))

# 设置响应编码格式  encoding
response.encoding = 'utf-8'

# 以字符串形式返回网页源码  text
print(response.text)

# 返回url地址   url
print(response.url)

# 返回二进制数据   content
print(response.content)

# 返回响应的状态码  status_code
print(response.status_code)

# 返回响应头     headers
print(response.headers)