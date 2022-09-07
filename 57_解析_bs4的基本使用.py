# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 8:44
# @Author : 程序猿阿辉
# @File : 57_解析_bs4的基本使用
# @Project : Python_Spider


# BeautifulSoup简称：bs4
#   与xml一样，bs4也是html的解析器，主要功能也是解析、提取数据


# 安装：
# pip install bs4

# 导入
# from bs4 import BeautifulSoup

# 导入bs4
from bs4 import BeautifulSoup

# 通过解析本地文件  将bs4基础语法进行详解
# 默认打开文件格式为jbk，打开文件时需要指定格式
soup = BeautifulSoup(open('57_解析_bs4的基本使用.html',encoding='utf-8'),'lxml')
# print(soup)

# 根据标签名字查找节点
# 返回第一个a标签
print(soup.a)
# 获取标签的值和标签属性值
print(soup.a.attrs)

# bs4的函数
# 1.find    返回第一个符合条件的数据
print(soup.find('a'))
# 根据title值找到对应标签值
print(soup.find('a',title='a2'))
# 在原本就有的关键字属性后添加下划线即可实现上述功能
print(soup.find('a',class_='a10086'))

# 2.find_all    以列表形式返回符合条件的所有数据
print(soup.find_all('a'))

# 获取多个标签数据，需在方法参数中以列表形式添加数据
print(soup.find_all(['a','span']))

# limit=n 查找前n个数据
print(soup.find_all('li',limit=2))

# 3.select（推荐）
# select返回一个列表  并且返回多个数据
print(soup.select('a'))

# 通过类选择器查找标签
print(soup.select('.a10086'))

# 通过id选择器查找标签
print(soup.select('#a123'))

# 属性选择器
# 查找li标签中有id的标签
print(soup.select('li[id]'))

# 查找li标签中id为a1234的标签
print(soup.select('li[id="a1234"]'))

# 层级选择器
# 后代选择器
# 找div下的li
print(soup.select('div li'))

# 子代选择器     某标签的第一级子标签
# ps：很多计算机编程语言中，选择器不加空格 没有返回值
print(soup.select('div > ul > li'))

# 找a标签和li标签所有对象
print(soup.select('a,li'))

# 节点信息
# 获取节点内容
# 标签对象中只有内容     string和get都可使用
# 标签对象中有内容也有数据      前者获取不到数据    后者可以
# 推荐使用get_text()
obj = soup.select('#d1')[0]
print(obj.string)
print(obj.get_text())

# 节点属性
obj = soup.select('#p1')[0]
# name      标签名字
print(obj.name)
# attrs     将属性值以字典形式返回
print(obj.attrs)

# 获取节点属性
obj = soup.select('#p1')[0]

print(obj.get('class'))
print(obj.attrs.get('class'))
print(obj['class'])




