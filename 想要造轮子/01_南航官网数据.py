# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 21:56
# @Author : 程序猿阿辉
# @File : 01_南航官网数据
# @Project : Python_Spider


# 在学习的过程中尝试自己动手爬一些网站的数据

# 本次需求：爬取南航官网上2022.09.07从广州飞往哈尔滨的航班批次、实际离地时间、计划起飞时间、实际到达时间、计划到达时间、始末地点

# 南航官网上找到接口：
# 航班批次 <div class="num item">       始发地点 <div class="dAirport item">
# 到达地点 <div class="aAirport item">  实际离地 <div class="depTime item"> span class="bold"
import time

url = 'https://b2c.csair.com/B2C40/modules/services/COD/flightStatus.html?c1=CAN&c2=HRB&d=2022-09-07&s=1'

import urllib.request
from lxml import etree

# 爬取时发现有反爬
# 请求对象定制

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
# request = urllib.request.Request(url=url,headers=headers)

# response = urllib.request.urlopen(url=url)

# content = response.read().decode('utf-8')
# print(content)

# 使用插件selenium
from selenium import webdriver
# 驱动文件路径
path = '../chromedriver.exe'
# 创建对象
# driver = webdriver.Chrome()
browser = webdriver.Chrome(path)
# time.sleep(20)

# 访问网站
browser.get(url)
# page_source   获取网页源码
content = browser.page_source

from selenium.webdriver.common.by import By
# 根据class找到数据
button = browser.find_element(By.__class__,'num item')
print(button)

# 解析服务器响应文件
# tree = etree.HTML(content)
#
# result = tree.xpath('//div//ul//li//div[@class="num item"]/text()')
#
# print(result)


