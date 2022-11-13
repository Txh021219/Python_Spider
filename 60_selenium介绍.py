# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 18:47
# @Author : 程序猿阿辉
# @File : 60_selenium介绍
# @Project : Python_Spider


# 什么是selenium
# 1.selenium是用于web应用程序测试的工具
# 2.selenium测试直接运行在浏览器，像真正的用户操作一样
# 3.支持通过各种driver,驱动真实浏览器完成测试
# 4.selenium支持无界面浏览器

# 模拟浏览器功能，自动执行网页中js代码，实现动态加载

import urllib.request

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')

print(content)

# 在获取到的网页源码中，并未发现京东秒杀模块中的标签属性J_seckill
# ctrl + F  查找  0个结果
# 这是由于服务器校验为非真正的内核浏览器，因此没有返回
# 此时可以用到selenium来驱动真正的浏览器获取源码
