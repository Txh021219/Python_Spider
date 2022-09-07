# _*_ coding : utf-8 _*_
# @Time : 2022/9/4 11:17
# @Author : 程序猿阿辉
# @File : 53_解析_获取百度网站之百度一下
# @Project : Python_Spider


# 1.获取网页源码
# 2.解析    解析服务器响应文件   etree.HTML
# 3.打印

import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟服务器向网站发送请求
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

# 解析网页源码(xpath)    获取需要的数据
# 导入lxml.etree
from lxml import etree

# 解析服务器响应文件
tree = etree.HTML(content)

# 获取所需数据    xpath返回值是一个列表类型数据
result = tree.xpath('//input[@id="su"]/@value')

print(result)