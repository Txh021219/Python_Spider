# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 16:49
# @Author : 程序猿阿辉
# @File : 28_函数返回值
# @Project : Python_Spider


# 返回值的关键字为return    存在函数中
def fun():
    print('111')
    return fun()

# 调用函数
print(fun())
# c = fun()
# print(c)也是可以的
# maximum recursion depth exceeded while calling a Python object
# 超过python最大递归深度