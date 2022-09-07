# _*_ coding : utf-8 _*_
# @Time : 2022/8/7 21:52
# @Author : 程序猿阿辉
# @File : 47_urllib_异常
# @Project : Python_Spider


# URLError\HTTPError
# 1.HTTPError类是URLError类的子类
# 2.导入的包为urllib.error.HTTPError    urllib.error.URLError
# 3.http错误：http错误是针对浏览器无法连接到服务器而增加出来的错误提示。
# 引导并告诉浏览者该页是哪里出了问题
# 4.通过urllib发送请求的时候，有可能会发送失败，这个时候如果想让你的代码更加的健壮，
# 可以通过try-expect进行捕获异常，异常有两类，URLError\HTTPError

import urllib.request
import urllib.error
# 另一种写法：
# from urllib import request,error

url = 'https://blog.csdn.net/m0_62218217/article/details/1258108161'

# url = 'http://www.Ahuishishuaibi.com'

headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 捕获异常
try:
    # 请求对象定制
    request = urllib.request.Request(url=url,headers=headers)

    # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)

    # 查看网页响应的数据
    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError as e:
    print('系统正在升级，请稍后再试！')
    print(e.reason)
except urllib.error.URLError:
    print('查无此网站，请您先建站！')


# HTTPError与URLError的区别：
# urlerror:产生的原因主要是1.网络没有连接，2服务器连接失败，3，找不到指定的服务器。
# httperror时urlerror的详细化的错误异常，url只能粗略的判断异常的原因，
# 而httperror可以 详细的判断异常并返回对应的状态码，可以清楚的知道http此时的状态。
# 所以常规思路是先使用httperror判断是否是http的问题，后使用urlerror

# 调用urllib.error.reason查看错误原因
# except urllib.error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')  # 使用httperror判断