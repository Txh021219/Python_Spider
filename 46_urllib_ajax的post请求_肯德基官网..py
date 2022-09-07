# _*_ coding : utf-8 _*_
# @Time : 2022/8/7 20:54
# @Author : 程序猿阿辉
# @File : 46_urllib_ajax的post请求_肯德基官网.
# @Project : Python_Spider
# 肯德基餐厅查询：按城市分：北京的接口第一页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post请求

# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 肯德基餐厅查询：按城市分：北京的接口第二页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post请求

# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

# 区别：每页中network->Payload->form Data中的pageIndex的值不同

import urllib.request
import urllib.parse

# base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }

    # 将data转换为unicode格式     使用urllib.parse.urlencode
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('kfc_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page,end_page + 1):
        # 请求对象定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(page,content)

# tips:
#         ctrl + alt + l  自动缩进