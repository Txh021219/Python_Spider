# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 14:56
# @Author : 程序猿阿辉
# @File : 71_requests_cookie登录古诗文网
# @Project : Python_Spider

# 需求：
# 通过登录  进入主页面

# 登陆时所需参数很多:
# __VIEWSTATE: xK6woaPWLSCU+nyX+rzepgZEwiKcgMBa5i4upFRjfcl1NMkOSIg0uM1U2ZQLR2yEGurixjN+8OjzzxepWsjbqVXh24Bt7rR/WxEDfmLLr8WTx4YfE8wu0HM3YT8YgK5bN/UZtcKyGlkCl2Z6jLAkMPNKIjE=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 13928593242
# pwd: 12354466
# code: THG3
# denglu: 登录

# __VIEWSTATE   __VIEWSTATEGENERATOR  code是变量

# 难点：1.__VIEWSTATE   __VIEWSTATEGENERATOR   一般情况下看不到的数据都在页面源码中
#         获取网页源代码 通过解析源码即可获取
#      2.code验证码

# 导入requests
import requests

# 登录页面的url
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
content = response.text

# 解析页面源码    获取所需的值      隐藏域的获取
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print(viewstate)
print(viewstategenerator)


# 验证码的获取    验证码在一个img标签下
# 验证码图片获取
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
# print(code_url)

# 将验证码图片下载到本地
# PS:在下载验证码图片时  相当于执行一次验证码  也就是验证码会更新   因此该方法无效
# 该方法不适合用于获取动态验证码   下载时视为执行一次操作，验证码动态刷新，所输入验证码与当前不符 无法登陆页面
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='71_code.jpg')

# requests中有个方法叫session()   通过session返回值    能使请求变成对象

session = requests.session()
# 验证码的url内容
response_code = session.get(code_url)
# 此时要使用二进制数据    因为需要下载图片    图片下载需要二进制
content_code = response_code.content
# wb格式      将二进制数据写入文件
with open('code.jpg','wb') as fp:
    fp.write(content_code)
# 获取验证码图片后，下载到本地，观察后在控制台输入验证码   就可以将该值给code参数   然后登录

code_name = input('请输入你的验证码：')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
   '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13928593242',
    'pwd': '1298035164make',
    'code': code_name,
    'denglu': '登录',
}

requests_post = session.post(url=url,headers=headers,data=data_post)

content_post = requests_post.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)


# 难点：1.两个隐藏域问题
#      2.动态验证码

