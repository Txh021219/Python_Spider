# _*_ coding : utf-8 _*_
# @Time : 2022/10/10 14:43
# @Author : 程序猿阿辉
# @File : 70_requests_代理
# @Project : Python_Spider

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=0C1E536A3019902F2449FEB79E511805; PSTM=1659272483; BAIDUID=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; BAIDUID_BFESS=0C1E536A3019902FDBD3F12B4DD86FCC:FG=1; ZFY=:BzZiAepwaK3ZviiTz0zqbehrG7cMq11ObchMQUCui1M:C; COOKIE_SESSION=196175_1_6_9_3_6_1_0_6_5_3_0_105836_0_0_0_1662532391_1662426543_1663665531%7C9%2362666_20_1662426541%7C5; BD_HOME=1; H_PS_PSSID=37548_36559_37561_36884_37403_36805_36786_37498_37508_26350_37450; BD_UPN=12314753; BA_HECTOR=a50l2ga1818l0l01852h83pl1hk7fkv1b; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_645EC=abfbN7dCS21cP3WCY7eVO8E9VFtg6UaCCdfKVVQ2R2xZi%2B9%2F60NRsxaO484; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; baikeVisitId=0293f9c4-dafa-496b-be5d-aebf0592d6b1; BDSVRTM=242'
}

data = {
    'wd':'ip'
}

# 代理ip的字典
proxy ={
    'http':'***代理的ip**:**代理端口**'
}

response = requests.get(url=url,headers=headers,params=data)

content = response.text

with open('80_daili.html','w',encoding='utf-8') as fp:
    fp.write(content)