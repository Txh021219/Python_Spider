# _*_ coding : utf-8 _*_
# @Time : 2022/8/6 21:14
# @Author : 程序猿阿辉
# @File : 43_urllib_post请求百度翻译_详细翻译
# @Project : Python_Spider


import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1659769211792_1659855150914_uBSkm5bbYc1qT79/0cUbm39J6U5EZgqbjE0yHYR74Fpf4sqUxzP91rMGWSUq6e7x8JO3UXDl0mgqiY5B+1URQwAjx82gzuYxBXPKViujvB++wbdu3quvmk+NkqNZPo+CwOWN8bxShIZsVSVORrIGUHTkARDXouOUcuTNbpFJHqlCzczoD9wvigyzlXhr7iQENoUKnzogyV7KQRw1QwM3f46n8mf9OLrxAuZvI9XxM4RihUa0KltvZSJs9NDRHrxjZ6RfE1SSltm0Zbrk4bNUN/jGBIJpSAOHPPCehRTDY2xqMxDg3U1m81NdpmAOVwXm',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=0C1E536A3019902F2449FEB79E511805; PSTM=1659272483; BAIDUID=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; BAIDUID_BFESS=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; ZFY=:BzZiAepwaK3ZviiTz0zqbehrG7cMq11ObchMQUCui1M:C; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=212h0h8l2k2h2ka5250m489e1heskjb17; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36559_36625_36726_37107_36413_36847_36954_36946_36165_36918_36919_36570_36805_36741_37055_26350_37095_36930_37022; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1659785298,1659785846,1659791354,1659855131; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1659855131; ab_sr=1.0.1_Njk2MDlkNTJlMzk5NDViM2Q5MmE0MmYzYTUxMGZkZDAxN2UwYjQxYThmNzBmN2U5MjQ2MjgxMzhmNzNjN2I5ZjZkNzU0ZGYwNmQzNDg5MmFjOGJiN2FhY2U5YzczNTg2NjdjNTJhOWY4MjZlYjMyZmUzNjllYjBjZjc4ZTFiZTZiZWYxNTIyNjZkZDc0MjhkZmI3NDhjODI1MmE1ZjhlMg==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '02acc07393010ab4c4354564feec0323',
    'domain': 'common'
}

# post请求的参数必须进行编码   并且调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# print(content)

import json

obj = json.loads(content)
print(obj)

# 最后得出，headers中的cookie值是百度翻译网站必须的表头