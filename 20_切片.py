# _*_ coding : utf-8 _*_
# @Time : 2022/7/31 15:50
# @Author : 程序猿阿辉
# @File : 20_切片
# @Project : Python_Spider


#切片     s[start_index:end_index:step]
s = 'hello python '

# 在切片中直接写一个下标
print(s[1])

#遵循左闭右开区间的规则
print(s[0:4+1])

# 从起始index/从头开始一直到结尾/结束index
print(s[1:])

print(s[:4])

# 步长step决定跳跃的幅度
print(s[0:6:3])