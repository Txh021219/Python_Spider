# _*_ coding : utf-8 _*_
# @Time : 2022/8/9 11:27
# @Author : 程序猿阿辉
# @File : 49_urrlib_handler处理器的基本使用
# @Project : Python_Spider


# 为什么学习handler
import urllib.request

# urllib.request.urlopen(url)
# 不能定制请求头
# urllib.request.Request(url,headers,data)
# 可以定制请求头
# Handler
# 定制更高级的请求头   随着业务逻辑的复杂 请求对象的定制已经满足不了需求（动态cookie
# 和代理不能使用请求对象定制）


# 需求：使用handler访问百度      获取网页源码

# 包含所需的模块   urllib.request
import urllib.request

# 定义url
url = 'http://www.baidu.com'

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# handler   build_opener    open

# 获取handler对象
handler = urllib.request.HTTPHandler()

# 通过handler获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)



