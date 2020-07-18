# 【不可变数据类型】
# 概念：源内存空间的数据不允许修改
#       如果想要修改数据，只能开辟新的内存空间
#       让变量重新引用新内存空间的地址
# 分类： str int float bool tuple

# 地址不同证明重新开辟了内存空间

# int
num1 = 100
print(id(num1))
num1 += 10
print(id(num1))

print('=' * 30)
# 元组
info_tuple = (10, 20)
print(id(info_tuple))

info_tuple += (100, 200)
print(id(info_tuple))

print('=' * 30)
# 【可变数据类型】
# 不需要重新开辟内存空间
# 类型： list dict
# 地址一样证明没有开辟新的内存空间

# 列表
info_list = [100, 200]
print(id(info_list))

info_list += [1000, 2000]
print(id(info_list))


"""
注意：
1.可变类型的数据变化是通过方法实现的
"""


