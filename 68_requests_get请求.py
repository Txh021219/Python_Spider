# _*_ coding : utf-8 _*_
# @Time : 2022/9/18 10:44
# @Author : 程序猿阿辉
# @File : 68_requests_get请求
# @Project : Python_Spider


# urllib
# 1.一个类型六个方法
# 2.get请求     code,urlencode
# 3.post请求    百度翻译
# 4.ajax的get请求
# 5.ajax的post请求
# 6.cookie登录  微博
# 7.代理    代理池

# requests
# 1.一个方法六个属性
# 2.get请求
# 3.post请求
# 4.代理
# 5.cookie    破解验证码

# 导入requests库
import requests

#定义基础url
url = 'https://www.baidu.com/s?'

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=0C1E536A3019902F2449FEB79E511805; PSTM=1659272483; BAIDUID=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; BAIDUID_BFESS=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; ZFY=:BzZiAepwaK3ZviiTz0zqbehrG7cMq11ObchMQUCui1M:C; BD_UPN=12314753; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1660031571,1662363886; BA_HECTOR=212h0g8125ah2h00042hvl211hid1p419; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=907250_2_7_9_5_7_1_0_6_5_1_0_105836_62661_0_0_1662532391_1662426543_1663469356%7C9%2362666_20_1662426541%7C5; B64_BOT=1; H_PS_645EC=44d3UwR%2Bc%2FkHoQd6VPv%2Byu9xLOMHtoHf2kKhLu3YBdYg40qRcLowdDSUToE; baikeVisitId=a1fc59bd-0c90-4d63-97f8-da2cfc6db82e; BD_HOME=1; H_PS_PSSID=36559_37355_36884_36570_36805_36786_37387_37244_37259_26350_37192_37223',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

data = {
    'wd':'北京'
}

# 获取网页源码    get(url,params,kwargs)
# url 请求资源路径
# params  参数
# kwargs  字典
response = requests.get(url=url,params=data,headers=headers)

response.encoding = 'utf-8'
content = response.text
print(content)

# 总结：
# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象定制
# 请求资源路径中的?可以去掉

