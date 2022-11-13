# _*_ coding : utf-8 _*_
# @Time : 2022/9/8 10:09
# @Author : 程序猿阿辉
# @File : 62_selenium_元素定位
# @Project : Python_Spider


# selenium元素定位:
#     自动化要做的就是模拟鼠标和键盘来操作这些元素,点击,输入等.操作这些元素前首先要找到它们
#     WebDriver提供很多定位元素的方法

# 新版本Selenium代码：
# 首先在文件头部引入By


from selenium import webdriver
from selenium.webdriver.common.by import By
# 定位id为username，class_name为password，tag_name为input的元素

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# 根据id找到对象
# 新版需要通过selenium里的by模块
button = browser.find_element(By.ID,'su')
print(button)

# 根据标签属性值获取对象
button = browser.find_element(By.NAME,'wd')
print(button)

# 根据xpath获取对象
button = browser.find_element(By.XPATH,'//input[@id="su"]')
print(button)
# find_elements会返回一个列表

# 根据标签名字获取对象
button = browser.find_elements(By.TAG_NAME,'input')
print(button)

# 根据css选择器获取对象      使用bs4语法
button = browser.find_element(By.CSS_SELECTOR,'#su')
print(button)

# 根据链接文本（a标签）获取对象
button = browser.find_element(By.LINK_TEXT,'地图')
print(button)