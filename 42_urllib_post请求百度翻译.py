# _*_ coding : utf-8 _*_
# @Time : 2022/8/6 19:14
# @Author : 程序猿阿辉
# @File : 42_urllib_post请求百度翻译
# @Project : Python_Spider


# Post请求
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

data = {
    'kw':'spider'
}

# Post请求的参数必须进行编码   即变成bytes字节型     调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)

# post请求的参数是不会拼接在url后面的 而是放在请求对象定制的参数中，即data参数
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

print(content)
# 字符串类型

# 字符串str->json对象

import json
obj = json.loads(content)
print(obj)