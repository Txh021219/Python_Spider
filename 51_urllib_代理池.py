# _*_ coding : utf-8 _*_
# @Time : 2022/8/12 20:53
# @Author : 程序猿阿辉
# @File : 51_urllib_代理池
# @Project : Python_Spider

import urllib.request

# 代理池   用一个列表写若干个代理url
proxies_pool = [
    {'https':'118.24.151.16817111'},
    {'https':'118.24.151.16817222'},
]

# 导入random库
import random

proxies = random.choice(proxies_pool)

print(proxies)

url = 'http://www.baidu.com/s?wd=ip'

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 想要使用代理    需要使用proxyhandler方法
# response = urllib.request.urlopen(request)

# 参数：proxies    提供的代理
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)
# 读取网站返回的消息
content = response.read().decode('utf-8')

# 保存到本地
with open('daili1.html','w',encoding='utf-8') as fp:
    fp.write(content)
