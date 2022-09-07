# _*_ coding : utf-8 _*_
# @Time : 2022/8/7 15:32
# @Author : 程序猿阿辉
# @File : 45_urllib_ajax的get请求_豆瓣电影前十页
# @Project : Python_Spider

# 获取当日豆瓣电影喜剧片专栏中前六十部电影的接口（每二十部为一个接口）

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=40&limit=20

# 可轻易发现规律：start=n对应的是开始的电影
# page  1   2   3   4
# start 0   20  40  60

# 发现规律：start与page间存在的关系
# start = (page - 1) * 20


# 下载豆瓣电影喜剧片前十页的数据的步骤：

# 1.请求对象定制
# 2.获取相应的数据
# 3.下载数据到本地

# 包含模块
import urllib.parse
import urllib.request

# 封装需要用到的函数

# 创建请求函数
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&'

    data = {
        'start':(page - 1) * 20,
        'limit':'20'
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request

# 获取响应内容函数
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

# 下载响应内容函数
def download(page,content):
    with open('douban_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)

# 程序的入口
if __name__ == '__main__':
    print('欢迎使用阿辉豆瓣影片爬虫1.0！')
    print('一页为20部电影！')
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入结束的页码：'))

    # 左闭右开区间，结束page要加一

    for page in range(start_page,end_page + 1):

#         每一页都要有自己的请求对象定制
         request = create_request(page)
#          获取相应的数据
         content = get_content(request)
#          下载
         download(page,content)

# tips:
#     在对应文件中按住ctrl + alt + l可实现自动缩进

