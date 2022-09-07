# _*_ coding : utf-8 _*_
# @Time : 2022/8/12 21:13
# @Author : 程序猿阿辉
# @File : 52_xpath的使用
# @Project : Python_Spider


# tips:xpath使用前先进行安装    不会下载求我

# 安装lxml库
# 方法：1.win+R输入cmd打开command prompt
#      2.输入以下内容：pip install lxml -i https://pypi.douban.com/simple
#      3.等待下载完成

# 导入lxml库
from lxml import etree

# xpath解析
# 1.本地文件    etree.parse()
# 2.服务器响应的数据  response.read().decode('utf-8')   etree.HTML()

# xpath解析本地文件
tree = etree.parse('52_xpath的使用.html')

# xpath严格遵守html双标签格式，单标签需添加/

# tree.xpath('xpath路径')

# //    查找子孙结点（任意子孙）
# /     查找直接结点

# 查找ul下的li
li_list = tree.xpath('//body/ul/li')
# body下的ul直接结点li


print(li_list)
# 判断列表长度
print(len(li_list))

# 查找所有有id属性的li标签
# text()获取标签中的内容
li_list = tree.xpath('//body/ul/li[@id]/text()')
print(li_list)
print(len(li_list))


# 查找id为l1的li标签
li_list = tree.xpath('//ul//li[@id="l1"]/text()')
print(li_list)
# ps:注意id属性引号的问题

# 查找id为l1的li标签的class属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')

print(li)

# 模糊查询
# 查找id属性里包含l的li标签

li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# contains(@标签属性，"包含内容")
print(li_list)

# 查询id值以l开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
# starts-with(@标签属性,"开头内容")

print(li_list)

# 逻辑运算
# 查询id为li和class为c1的标签
li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# 和 and连接
print(li_list)

li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
# 或 | 连接        针对标签属性，需要分开来写
print(li_list)