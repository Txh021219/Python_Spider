# _*_ coding : utf-8 _*_
# @Time : 2022/8/9 15:06
# @Author : 程序猿阿辉
# @File : 50_urllib_代理
# @Project : Python_Spider


# 代理的常用功能：
# 1.突破自身IP访问限制，访问国外站点；
# 2.访问一些单位或团体内部的资源
#     拓展：某大学FTP（前提是该代理地址在该资源的允许访问范围内），使用教育网内地址段免费代理服务器
#          就可以用于对教育网开放的各类FTP下载上传，以及各类资源共享等服务。
# 3.提高访问速度：
#     拓展：通常代理服务器设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，
#     　　　当其他用户在访问相同的信息时，则直接由缓冲区中取出信息，传给用户，以提高访问速度
# 4.隐藏真实IP：
#     拓展：上网者也可以通过该方法隐藏自己的IP，以免被攻击

# 本地ip
# https://www.baidu.com/s?wd=ip

import urllib.request

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip'

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)

# handler   build_opener    open
# ProxyHandler(proxies) proxies是代理  以字典形式存在

proxies = {
    'http':'116.20.14.237:49688'
}
handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取网页响应信息
content = response.read().decode('utf-8')

# 保存到本地
with open('daili1.html','w',encoding='utf-8') as fp:
    fp.write(content)