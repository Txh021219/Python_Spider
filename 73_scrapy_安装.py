# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 10:58
# @Author : 程序猿阿辉
# @File : 73_scrapy_安装
# @Project : Python_Spider

# 安装：pip install scrapy -i https://douban.com/siple

# 安装可能出现的问题：
# 1.报错  building''twisted.test.raiser' etension
#     缺少 twisted库
# 解决：下载 https://www.lfd.uci.edu/~gohlke/pythonlibs/
#       对应版本whl文件 twisted_iocpsupport‑1.0.2‑cp39‑cp39‑win_amd64.whl
#       下载完成后 pip install + 路径 如：pip install D:\Py\twisted_iocpsupport-1.0.2-cp39-cp39-win_amd64.whl
#       安装完twisted后再次安装scrapy
#   其他问题上网查

