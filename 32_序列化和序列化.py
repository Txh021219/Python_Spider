# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 20:03
# @Author : 程序猿阿辉
# @File : 32_序列化和序列化
# @Project : Python_Spider

# 文件操作时，可将字符串写入一个本地文件中。但如果是一个对象（如列表、元组、字典等），无法直接写入文件中，这种情况要先将对象进行序列化，才能写入文件
# 序列化：设计一套协议，按照某种规则，把内存中的数据转换为字节序列，保存到文件，就是序列化
# 反序列化：从文件的字节序列恢复到内存中，就是反序列化

# python中提供JSON模块实现数据序列化与反序列化

# JSON模块    JavaScriptObjectNotation,JS对象简谱     一种轻量级数据交换标准。
# JSON本质是字符串

# fp = open('text.txt','w')
# # 默认情况下只能把字符串str写入文件中
# fp.write('hello!' * 3)
#
# fp.close()

#序列化的两种方式
# dumps()   dump()
# 创建一个文件
fp = open('text.txt', 'w')

name_list = ['cxk','wyf']

# 导入JSON模块到文件中
import json

# 序列化
# 将python对象 变成  json字符串
# 在使用scrapy框架时  该框架返回一个对象   要将对象写入到文件中  就要使用json.dumps
names = json.dumps(name_list)
print(names)
# 打印得names类型为str
print(type(names))

# 将names写入文件中
fp.write(names)

fp.close()


# dump()
# 在将对象转换为字符串的同时，指定一个文件的对象，然后将转换后字符串写入该文件中

fp = open('text.txt','w')

name1_list = ['asd','asff']

import json

json.dump(name1_list,fp)
# json.dump(对象名称,要写入文件名称)

fp.close()


# 反序列化
# 将json字符串转换为python对象

fp = open('text.txt','r')

content = fp.read()
fp.close()

# str类型
print(content)
print(type(content))


# loads()
import json
# 将json字符串变成python对象

result = json.loads(content)
# list类型
print(result)
print(type(result))





# load()
fp = open('text.txt','r')
import json
result = json.load(fp)
fp.close()

print(result)
print(type(result))
