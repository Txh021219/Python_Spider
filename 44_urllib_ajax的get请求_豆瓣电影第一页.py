# _*_ coding : utf-8 _*_
# @Time : 2022/8/7 15:13
# @Author : 程序猿阿辉
# @File : 44_urllib_ajax的get请求_豆瓣电影第一页
# @Project : Python_Spider


# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
# get请求
# 获取豆瓣电影第一页数据   保存起来

import urllib.request

# 网页url
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# 网页标头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

# 数据下载到本地
# open方法默认使用gbk编码   如果想保存汉字 需要再open方法中指定编码格式为utf-8
# encoding = 'utf-8'
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open('douban.json','w',encoding='utf-8') as fp:
    fp.write(content)