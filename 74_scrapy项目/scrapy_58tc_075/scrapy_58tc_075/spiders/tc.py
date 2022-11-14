import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://dg.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B']
    start_urls = ['https://dg.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B']

    def parse(self, response):
        # print('坤坤来啦！')
        # 字符串
        # content = response.text

        #二进制数据
        # content = response.body
        print('*******************************')
        # print(content)

        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print(span)