# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 14:35
# @Author : 程序猿阿辉
# @File : 58_解析_bs4爬取星巴克数据
# @Project : Python_Spider

# 导入模块
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

request = urllib.request.urlopen(url)

content = request.read().decode('utf-8')

# 使用bs4
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# xpath插件下的类选择器
# //ul[@class="grid padded-3 product"]//strong/text()
# 转换为bs4格式
name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    # 可调用get_text()来获取strong标签下的内容
    print(name.get_text())