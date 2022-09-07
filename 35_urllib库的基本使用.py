# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 10:51
# @Author : 程序猿阿辉
# @File : 35_urllib库的基本使用
# @Project : Python_Spider


# 使用urllib获取百度首页源码
import urllib.request

# 定义url     要访问的地址
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求     response    响应
response = urllib.request.urlopen(url)

# 获取响应中页面的源码    content     内容
# read方法    返回的是字节形式的二进制数据
# 要将二进制数据转换为字符串
# 二进制->字符串      解码      方法：decode('编码格式')
content = response.read().decode('utf-8')
print(content)