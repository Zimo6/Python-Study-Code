# 字符串操作
string = "hello cuishuangqi"
# 1、【查询字符串】
# 1.1 根据内容查下标
print(string.find('c'))     # 找到了返回最左边字符的索引，没找到返回-1
print(string.find('c', 2, 10)) # 从指定位置找
print(string.index('cui'))      # 与find类型，但是找不到会报错
print(string.index('c', 2, 10))
# 1.2 根据下标查内容（注意索引越界）
print(string[6])

print('=========分割线==========')

# 2、【统计字符串】
# 2.1 统计长度
print(len(string))
# 2.2 统计子字符串出现次数
print(string.count('h'))
print(string.count('h', 2, 5))  # 统计下标某个范围

print('=========分割线==========')

# 3、【字符串的替换】 源字符串内容不变
my_str = "Hello word word"
# 3.1判断字符换开始和结尾
print(my_str.startswith('Hello'))   # 返回值为True或False
print(my_str.endswith('qo'))        # 返回值为True或False
# 3.2 字符串的替换
print(my_str.replace('word', 'cuishuangqi'))
print(my_str.replace('word', 'cuishuangqi', 1)) # 指替换一次
# 3.2 字符串大小写转换
print(my_str.upper())   #转换为大写
print(my_str.lower())   #转换为小写

print('=========分割线==========')

# 4、【字符串的切分与拼接】 源字符串内容不变
# 4.1 切分
my_str = "hello,wo,shi,sh\rui"
print(my_str.split(','))    # 返回为一个列表
print(my_str.split(',', 1))  # 只切一次
print(my_str.splitlines())  # 按照（'\r' '\n' '\r\n' 切割）
# 4.2 字符串拼接
my_str1 = 'hello'
my_str2 = 'word'
print(my_str1 + my_str2)
print('%'.join(my_str1)) # h%e%l%l%o

print('=========分割线==========')

# 5 【字符串切片】
# string[起始索引:结束索引:步长]  范围为左闭右开 [1,3)
print(string[0:2])
print(string[:-1])
print(string[::-1])  # 字符串倒序