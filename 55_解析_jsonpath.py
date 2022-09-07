# _*_ coding : utf-8 _*_
# @Time : 2022/9/6 8:58
# @Author : 程序猿阿辉
# @File : 55_解析_jsonpath
# @Project : Python_Spider


# jsonpath安装使用方式：

# pip安装
# pip install jsonpath
#
# jsonpath使用：
#     obj = json.load(open('json文件','r'.encoding='utf-8'))
#     ret = jsonpath.jsonpath(obj,'jsonpath语法')

# 教程参考：https://blog.csdn.net/Obstinate_L/article/details/125294971?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166242656316781432991968%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166242656316781432991968&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-125294971-null-null.142^v46^pc_rank_34_default_2&utm_term=jsonpath%E7%AE%80%E5%8D%95%E5%85%A5%E9%97%A8&spm=1018.2226.3001.4187

# 导入json、jsonpath
import json
import jsonpath

obj = json.load(open('55_解析_jsonpath.json','r',encoding='utf-8'))

# 需求：json文件下书店所有书的作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)

# json文件下所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下所有元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)

# store下所有东西的price
price_list = jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# store下book中第三本书
book = jsonpath.jsonpath(obj,'$.store.book[2]')
print(book)

# 最后一本书
book = jsonpath.jsonpath(obj,'$.store.book[(@.length-1)]')
print(book)

# 前两本书
book_list = jsonpath.jsonpath(obj,'$..book[0,1]')
# book_list = jsonpath.jsonpath(obj,'$..book[:2]')
print(book_list)

# 过滤出所有包含isbn的书
# 条件过滤需在括号()前添加问号?
book_list =jsonpath.jsonpath(obj,'$store..book[?(@.isbn)]')
print(book)

# 哪些书超过十块钱
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)
