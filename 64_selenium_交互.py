# _*_ coding : utf-8 _*_
# @Time : 2022/9/14 10:24
# @Author : 程序猿阿辉
# @File : 64_selenium_交互
# @Project : Python_Spider

# selenium交互        适配：网页懒加载等

# 先导入selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 定义url
url = 'https://www.baidu.com'
browser.get(url)
import time
# 等待2s
time.sleep(2)

# 获取文本框对象
input = browser.find_element(By.ID,'kw')

# 在文本中输入周杰伦
input.send_keys('周杰伦')
time.sleep(2)

# 获取百度一下按钮
button = browser.find_element(By.ID,'su')

# 点击按钮
button.click()
time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)

# 利用xpath获取下一页按钮
next = browser.find_element(By.XPATH,'//a[@class="n"]')

# 点击下一页
next.click()
time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)

# 返回上一步
browser.forward()
time.sleep(2)

# 退出
browser.quit()