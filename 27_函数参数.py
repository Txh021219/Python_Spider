# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 16:39
# @Author : 程序猿阿辉
# @File : 27_函数参数
# @Project : Python_Spider


# 使用函数计算1和2的和

# 定义函数
def sum(a,b):
    c = a + b
    print(c)


# 位置传参      按照位置一一对应关系传递参数
a = int(input('请输入a的值'))
b = int(input('请输入b的值'))
# 调用函数
sum(a,b)

# 关键字传参
sum(a=100,b=200)

# 定义函数时a,b称为形式参数
# 调用函数时a,b的具体值成为实际参数