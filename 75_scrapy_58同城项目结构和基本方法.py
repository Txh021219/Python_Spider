# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 20:20
# @Author : 程序猿阿辉
# @File : 75_scrapy_58同城项目结构和基本方法
# @Project : Python_Spider



# 在58同城网站找到接口
# https://dg.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B

# 在终端cd到所选文件夹
# 在所选文件夹中利用cmd终端新建58同城项目文件夹 eg:scrapy startproject scrapy_58tc_075
# cd到spiders文件夹下
# 创建爬虫文件 scrapy genspider tc https://dg.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_B
# scrapy genspider 爬虫文件名称 url接口
# 运行爬虫  scrapy crawl tc     注意君子robot协议

# 1.scrapy项目结构
# 项目名字
#     项目名字
#         spiders文件夹(存储自定义爬虫文件)
#             init文件
#             $*自定义爬虫文件 核心功能文件*$
#         init文件
#         items   定义数据结构  爬取数据都包含什么
#         middleware  中间件 代理
#         pipelines   管道  处理下载的数据
#         settings    配置文件    robots协议    ua定义等

# response属性和方法
#     response.text    获取响应的字符串
#     response.body    获取二进制数据
#     response.xpath    直接使用xpath方法解析response中的内容
#     response.extract()    提取seletor对象的data属性值
#     response.extract_first()  提取seletor列表中的第一个数据