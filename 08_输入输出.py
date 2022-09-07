# _*_ coding : utf-8 _*_
# @Time : 2022/7/29 21:11
# @Author : 程序猿阿辉
# @File : 08_输入输出
# @Project : Python_Spider

# 普通输出
print('Jay的歌真好听！')

# 格式化输出
# scrapy框架      excel文件     mysql       redis
boold = 'B'
age = 20
# %s    字符串     %d      数值
print('我的血型是%s，年龄是%d' % (boold,age))


#输入
# input方法输入的内容默认为str字符串格式
who = input('你是谁')
print(who)