import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名字  用于于宁爬虫时使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址  指第一次要访问的url
    # start_urls是在allowed_domains前加http//
    #             在allowed_domains后加/
    start_urls = ['http://www.baidu.com/']
    # 执行起始url后执行的方法 方法中response是返回的url对象
    # 相当于response = url*****
    def parse(self, response):
        pass