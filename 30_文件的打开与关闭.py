# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 17:52
# @Author : 程序猿阿辉
# @File : 30_文件的打开与关闭
# @Project : Python_Spider


# open(文件路径，访问模式)
# open(file,mode,buffering...)

# 访问模式：
#             w   可写
#             r   可读

# 创建一个test.txt文件
# 文件夹不能被创建

fp = open('test.txt','w')
print(fp)

fp.write('做我女朋友吧')
print(fp)

# 文件的关闭
# 有开就有关
fp.close()
print(fp)
