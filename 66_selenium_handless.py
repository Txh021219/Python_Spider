# _*_ coding : utf-8 _*_
# @Time : 2022/9/18 9:52
# @Author : 程序猿阿辉
# @File : 66_selenium_handless
# @Project : Python_Spider


# 该插件有固定格式如下：
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('__headless')
chrome_options.add_argument('__disable-gpu')

# path为用户chrome浏览器文件路径，自行修改
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

# 该方法已被弃用   使用options代替
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')

# 封装handless

#导入模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#封装固定格式
def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('__headless')
    chrome_options.add_argument('__disable-gpu')

    # path为用户chrome浏览器文件路径，自行修改
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    # 该方法已被弃用   使用options代替
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome(options=chrome_options)
    return browser

# 定义url
url = 'https://www.baidu.com'

# 获取网页源码
browser.get(url)