# _*_ coding : utf-8 _*_
# @Time : 2022/8/1 11:20
# @Author : 程序猿阿辉
# @File : 37_urllib库_下载
# @Project : Python_Spider


import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url代表下载路径     filename代表文件名字
# urllib.request.urlretrieve(url,filename=None,reporthook=None,data=None)
# python中可以写文件名 也可以直接写值
# def callback(blocknum, blocksize, totalsize):
#     '''
#     :param blocknum: 已下载数据块
#     :param blocksize: 数据块大小
#     :param totalsize: 远程文件大小
#     :return:
#     '''
#     percent = 100.0*blocknum*blocksize/totalsize
#     if(percent>100):
#         percent = 100
#     print('%.2f%%' % percent)
#
# url = 'http://www.sina.com.cn'
# local = 'f:\\sina.html'
# a,b = urllib.request.urlretrieve(url, local, callback) #从远程下载数据
# urllib.request.urlretrieve(url_page,'baidu.html')


# 下载图片
url_img = 'https://img2.baidu.com/it/u=1814268193,3619863984&fm=253&fmt=auto&app=138&f=JPEG?w=632&h=500'

# urllib.request.urlretrieve(url= url_img,filename= 'img.jpg')

# 下载视频
url_vedio = 'https://www.bilibili.com/video/BV1Mk4y1o7m8?t=592.5'

# urllib.request.urlretrieve(url_vedio,'asmr.avi')
