# _*_ coding : utf-8 _*_
# @Time : 2022/9/18 11:08
# @Author : 程序猿阿辉
# @File : 69_requests_post请求
# @Project : Python_Spider


# 导入requests库
import requests

# 定义url
url = 'https://fanyi.baidu.com/sug'

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求获取源码    post(url,data,json,kwargs...)
# url     请求路径
# data    请求参数
# kwargs  字典
response = requests.post(url=url,data=data,headers=headers)

content = response.text
# print(content)
# json格式转化为utf-8
import json
obj = json.loads(content.encode('utf-8'))
print(obj)

# 总结：
# 1.post请求不需要编、解码
# 2.post请求参数是data
# 3.不需要请求对象定制
