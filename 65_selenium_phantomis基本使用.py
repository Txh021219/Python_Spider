# _*_ coding : utf-8 _*_
# @Time : 2022/9/16 10:49
# @Author : 程序猿阿辉
# @File : 65_selenium_phantomis基本使用
# @Project : Python_Spider


# 什么是phantomjs
#     1.是一个无界的浏览器
#     2.支持页面元素查找，js的执行等
#     3.由于不进行css和gui渲染，运行效率要比真实浏览器快得多

from selenium import webdriver

path = 'phantomjs.exe'

# 由于新版本selenium已不支持phantomjs，而且该插件已经基本被弃用，因此这里不展开
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)