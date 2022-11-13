# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 19:00
# @Author : 程序猿阿辉
# @File : 61_selenium基本使用
# @Project : Python_Spider


# 操作谷歌浏览器的驱动    根据浏览器版本下载   向下兼容
# https://chromedriver.storage.googleapis.com/index.html

# 安装selenium
# pip install selenium

# 导入selenium
from selenium import webdriver

# 创建浏览器操作对象

# 驱动文件路径
path = 'chromedriver.exe'
# 创建对象
browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.jd.com/'

browser.get(url)

# page_source   获取网页源码
content = browser.page_source
print(content)