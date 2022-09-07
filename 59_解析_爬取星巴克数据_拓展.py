# _*_ coding : utf-8 _*_
# @Time : 2022/9/7 14:51
# @Author : 程序猿阿辉
# @File : 59_解析_爬取星巴克数据_拓展
# @Project : Python_Spider


# 本期拓展要点：
# 1.爬取星巴克官网菜单里的商品图片
# 2.爬取星巴克官网菜单里的商品名称
# 3.将商品和其名称一一对应，放在建好的文件夹中

# 导入所需模块
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

# 模拟浏览器向服务器发送请求
request = urllib.request.urlopen(url=url)
# 获取返回的网站源码
content = request.read().decode('utf-8')

# 在浏览器访问官网,获取接口
# 先抓取名称接口
# 发现商品名称在不同ul标签下都有一个相同的标签属性：grid padded-3 product
soup = BeautifulSoup(content,'lxml')

name_list = soup.select('div ul[class="grid padded-3 product"] strong')


# for name in name_list:
#     print(name.get_text())

# 获取图片接口
# 发现：在官网菜单与名称接口相同div下的li标签，下级的div标签有个属性：class="preview circle"
# 另一个属性中记录着url接口
# style="background-image: url("/images/products/xxx.jpg")"
# 因此：可以通过class或者style属性来取得源代码

# 同上
# soup = BeautifulSoup(content,'lxml')

img_list = soup.select('div ul[class="grid padded-3 product"] div[class="preview circle"]')

# 由于图片的接口是写在标签属性上的，因此要获取标签属性内容，然后切片、拼接字符串
# print(img_list[0].get('style'))

# background-image: url("/images/products/affogato.jpg")


for i in range(len(img_list)):
    img = img_list[i]
    name = name_list[i].get_text()
    # 对于文件命名，windows系统有不能出现的字符，因此需要转换   用法参考14_字符串高级
    if name.find('/' or':' or '*' or '?' or'"' or'<' or '>' or '|'or'$'or'\''):
        name = name.replace('/' or':' or '*' or '?' or'"' or'<' or '>' or '|'or'$'or'\'','$')
    # print(name)
    # 对标签内容切片
    img = img.get('style')[23:]
    n = len(img)
    img = img[:n-2]
    img_url = 'https://www.starbucks.com.cn' + img
    # print(img_url)
#     下载到本地
    urllib.request.urlretrieve(url=img_url,filename='./59_解析_爬取星巴克数据_拓展/' + name + '.jpg')

# https: // www.starbucks.com.cn / images / products / cold - brew.jpg
