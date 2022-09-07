# _*_ coding : utf-8 _*_
# @Time : 2022/9/6 9:40
# @Author : 程序猿阿辉
# @File : 56_解析_jsonpath解析淘票票
# @Project : Python_Spider

import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1662428546246_63&jsoncallback=jsonp64&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

# 请求头中，除了UA校验，也许会有其他校验，其中开头是冒号的，一般不能用
headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1662428546246_63&jsoncallback=jsonp64&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=Nj99Gz+9BnICAXQUDrOwUgj5; t=d38969917f1e35ef01b0b840d884bea4; cookie2=108f6b4d3d4f92523ed40240f506b60a; v=0; _tb_token_=333a365b3d91e; xlly_s=1; tfstk=cWPhBSjXJJkC6UTMZJGCaYJRv36OZ7WEA7Pa_wh3ejaoA0VNiVJw3_7CSDIfYL1..; l=eB_TwNTnLvG3JfkNBOfwlurza77tcIRAguPzaNbMiOCPOD5p5AqdW6kPoXY9CnGVhsMXR3z1UrspBeYBqC2sjqjqnZ2bjXHmn; isg=BDY2XHm7SZdZiTwTgbijcAhHh2w4V3qRyHTwfqAfSpm049Z9COYIodOd-7-Py3Kp',
    'referer': 'https://www.taobao.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

#请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向网站发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 直接打印获取的数据，开头的jsonp(和末尾);不是json内容，需要去掉
# print(content)

# 可以使用split方法切割字符串
content = content.split('(')[1].split(')')[0]
# print(content)

# 将获取的json数据保存到本地
with open('56_解析_jsonpath解析淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

#导入json加载json文件
import json
import jsonpath

obj = json.load(open('56_解析_jsonpath解析淘票票.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)
