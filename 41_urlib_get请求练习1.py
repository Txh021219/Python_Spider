# _*_ coding : utf-8 _*_
# @Time : 2022/8/2 19:16
# @Author : 程序猿阿辉
# @File : 41_urllib_get请求练习1
# @Project : Python_Spider


# 为了巩固对urllib.request   urllib.parse    等内容
# 特意创建自主练习1
# 目标：实现对输入的网页的内容进行爬取
# 要求：1.网址和关键字可以任意修改
#      2.打印网站源码


# *************************************************************************

# 包含库
import urllib.request
import urllib.parse
# 定义网址url
base_url = input('请输入要爬取网站的url:')
# 为实现对基础网址的补全，调用“字符串高级”中的endswith方法，作用是判断字符串是否以某结尾，是则返回true,否则false
# 还用到if流程控制语句
# if not base_url.startswith('http') or base_url.startswith('https'):
#     if base_url.startswith('http:') or base_url.startswith('https:'):
#         base_url = base_url + '/'
#     elif base_url.startswith('http') or base_url.startswith('https'):
if not base_url.endswith('/s?'):
    if base_url.endswith('/'):
        base_url = base_url + 's?'
    elif base_url.endswith('s'):
          base_url = base_url +'?'
    else:
        base_url = base_url +'/s?'

# 打印基础网址
print(base_url)

# 定义关键字数据字典
data = {
    'wd':input('请输入要搜索的内容：')
}

# # 为实现字典增加，调用“字典高级_增加”中的方法
# # 和while循环
# choice = True
# i = 1

# 字典data中键值对字符串转换为unicode格式
new_data = urllib.parse.urlencode(data)

# 完整url拼接
url = base_url + new_data
# 打印完整url
print(url)

#串头设置
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}

# 请求对象定制(url，headers)
request = urllib.request.Request(url=url,headers=headers)

# 模拟服务器向网站发送请求
response = urllib.request.urlopen(request)

# 获取网页源码资源(read读取网页源码,decode转换为utf-8)
content = response.read().decode('utf-8')

# 打印获取到的网页源码
print(content)
