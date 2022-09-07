# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 20:46
# @Author : 程序猿阿辉
# @File : 33_异常
# @Project : Python_Spider


# fp = open('aaa.txt','r')
#
# fp.read()
#
# fp.close()
# # FileNotFoundError: [Errno 2] No such file or directory: 'aaa.txt'
# # 没有找到文件的异常


#异常的格式：
try:
    fp = open('aaa.txt','r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级，请稍后再试！')