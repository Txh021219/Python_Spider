# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 11:34
# @Author : 程序猿阿辉
# @File : 74_scrapy_基本使用
# @Project : Python_Spider


# 在终端中创建对应项目    项目名称不能为数字不能含有汉字
# 1.在终端输入scrapy startproject scrapy_baidu_074 创建项目
# 2.创建爬虫文件  在爬虫文件spider中创建  cd scrapy_baidu_074\scrapy_baidu_074\spiders 进入爬虫文件
# scrapy genspider 爬虫文件名字   要爬取的网页url
# eg: scrapy genspider baidu www.baidu.com  不需要写https   域名自动添加
# 3.运行爬虫 scrapy crawl 爬虫名字 eg:scrapy crawl baidu
# 发现会有反爬：君子协定robots.txt 在settings中注释掉君子协定robots

