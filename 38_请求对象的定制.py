# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 15:09
# @Author : 程序猿阿辉
# @File : 38_请求对象的定制
# @Project : Python_Spider


import urllib.request

# 1.定义要爬取的网站url
url = 'https://www.baidu.com'

# url的组成
# http/https    www.baidu.com   80/443      s
#   协议                主机      端口号     路径      参数      锚点
# http                            80
# https                           443
# mysql                           3306
# oracle                          1521
# redis                           6379
# mongodb                         21017

# 2.定义网站识别浏览器信息的特殊字符串头（反爬手段）字典  添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}

# 因为urlopen方法中不能存储字典    所以headers不能传递进去
# 请求对象的定制(针对反爬的一种手段）
# 注意：由于参数顺序的原因，不能直接写url和headers 中间还有data    所以需要关键字传参
# 3.将headers字典模拟浏览器信息的请求头放进Request方法    得到一个Request
request = urllib.request.Request(url=url,headers=headers)
# print(request)
# print(type(request))

# 4.模拟浏览器向网站发送响应请求  返回一个HTTPresponse类型的数据
response = urllib.request.urlopen(request)
# print(type(response))
# print(response)

# 5.将HTTPresponse类型数据通过read()方法转换为二进制字符串，再通过decode('编码格式')方法转换为对应格式字符串
content = response.read().decode('utf-8')

# 6.打印提取到的网站源码
print(content)

# UA介绍：User Agent中文名是用户代理，简称UA，是一个特殊字符串头，使得服务器能识别客户使用的操作系统及版本
# 、cpu类型、浏览器及版本。浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等
# 语法：request = urllib.request.Request()
