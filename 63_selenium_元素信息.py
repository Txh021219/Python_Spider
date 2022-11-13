# _*_ coding : utf-8 _*_
# @Time : 2022/9/10 15:46
# @Author : 程序猿阿辉
# @File : 63_selenium_元素信息
# @Project : Python_Spider

# 导入selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 定义url
url = 'https://www.baidu.com'

# 驱动浏览器访问网站
browser.get(url)

# 查找元素
input = browser.find_element(By.ID,'su')

# 获取标签属性    get_attribute('元素属性')
print(input.get_attribute('class'))
# 获取标签名称
print(input.tag_name)
# 获取元素文本        即标签<>中的文本内容
a = browser.find_element(By.LINK_TEXT,'新闻')
print(a.text)




