# _*_ coding : utf-8 _*_
# @Time : 2022/9/5 15:47
# @Author : 程序猿阿辉
# @File : 54_解析_站长素材
# @Project : Python_Spider


# 1.请求对象定制
# 2.获取网页源码
# 3.下载到本地

# 需求    下载前十页图片
# 第一页：
# https://sc.chinaz.com/tupian/weimeiyijingtupian.html
# 第二页：
# https://sc.chinaz.com/tupian/weimeiyijingtupian_2.html
# 第三页：
# https://sc.chinaz.com/tupian/weimeiyijingtupian_3.html

import urllib.request
from lxml import etree
def create_request(page):
    if page==1:
        url=' https://sc.chinaz.com/tupian/weimeiyijingtupian.html'
    else:
        url=' https://sc.chinaz.com/tupian/weimeiyijingtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
# 下载图片
#   urllib.request.urlretrieve('图片地址','文件名字')
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@class="container"]//img/@alt')

    # 一般涉及图片网站都会进行懒加载
    img_list = tree.xpath('//div[@class="container"]//img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        img = img_list[i]
        # 获取到的图片地址无https：前缀
        url = 'https:' + img
        print(name,url)
#         下载到本地
        urllib.request.urlretrieve(url=url,filename='./54_站长素材图片保存/' + name + '.jpg')

# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page,end_page+1):
        #请求对象定制
        request = create_request(page)
        #获取网页源码
        content = get_content(request)
        down_load(content)

