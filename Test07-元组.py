# 【元组】
# 元组和列表一样，但是数据存储之后不能改变
# 定义
my_tuple = (100, 12.3, "python", False)
my_tuple1 = tuple()     # 面向对象定义，空元组
my_tuple2 = (100, )     # 只有一个元素的元组
print(my_tuple)
print(type(my_tuple))
# 访问列表元素（注意索引越界）
print(my_tuple[0])
# 元组切片
print(my_tuple[0:3])

# 列表的相关操作元组同样支持