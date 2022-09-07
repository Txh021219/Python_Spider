# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 15:39
# @Author : 程序猿阿辉
# @File : 39_get请求的quote方法
# @Project : Python_Spider


# 需求：获取https://www.baidu.com/s?wd=周杰伦的网页源码

import urllib.request

url = 'https://www.baidu.com/s?wd='


# 请求对象定制    为解决反爬虫的第一种手段
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}

# *************************************************************************
# 将周杰伦三字变成unicode编码格式
# 依赖urllib.parse.quote      将字符串转换为unicode格式
name = urllib.parse.quote('周杰伦')

url = url + name
#**************************************************************************

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

# 打印数据
print(content)