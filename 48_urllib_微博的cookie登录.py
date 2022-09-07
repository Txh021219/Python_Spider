# _*_ coding : utf-8 _*_
# @Time : 2022/8/9 10:52
# @Author : 程序猿阿辉
# @File : 48_urllib_微博的cookie登录
# @Project : Python_Spider


# 适用场景：数据采集时，需要绕过登录，然后进入到某个页面
# 个人信息页面是utf-8  但还是编码报错     因为没有转到个人信息页面    而是转到了登陆页面
# 登陆页面不是utf-8   所以报错

# 什么情况下访问不成功？
# 请求头信息不足时  访问不成功

import urllib.request

url = 'https://weibo.cn/5684712446/info'

headers = {
    # ':authority': 'weibo.cn',
    # ':method': 'GET',
    # ':path': '/5684712446/info',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
# cookie中携带登录信息     如果有登陆之后的cookie  就可以携带cookie进入任何登陆后的页面
    'cookie': '_T_WM=a1b05bc10f9009dfb7dad2e53e011ddd; SUB=_2A25P9bwIDeRhGeNI41YW8SzIzzqIHXVtGcRArDV6PUJbktANLWikkW1NSDHlvVUQBSrZaEj-hmXyBNhvWU40gkcN; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWmnigyzp6894bGOrMIbXs85NHD95QfSonXS02EShBcWs4Dqcj_i--Ni-iFiK.4i--Xi-i2i-27i--fiK.ciKLhi--Xi-z4iKyFi--4iKn0iKy8; SSOLoginState=1660013656',
# referer   判断当前路径是否通过上一路径进入    一般情况下是作图片防盗链
    'referer': 'https://weibo.cn/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# cookie中携带登录信息     如果有登陆之后的cookie  就可以携带cookie进入任何登陆后的页面
# referer   判断当前路径是否通过上一路径进入    一般情况下是作图片防盗链

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 向网页模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 查看网页响应的数据
content = response.read().decode('utf-8')

# print(content)

# 将数据保存到本地
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)

