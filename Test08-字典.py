# 【字典】  无序
#  键值对的方式存储数据
my_dict = {
    'name': '崔双麒',
    'age': 20,
    'gender': '男',
    'high': 180,
    'high': 200
}
print(my_dict)
print(type(my_dict))
"""
注意事项：
1、字典的key不能是列表、元组或字典本身，value可以是任意数据类型
2、重复的key所对的值会被覆盖
"""
# 访问字典
print(my_dict['name'])  # 不存在则报错
print(my_dict['gender'])  # 不存在则报错
print(my_dict.get('addr'))  # 不存在返回None，不会报错
print(my_dict.get('addr', "红安市"))  # 不存在返回后面的默认值，不会报错

# 增/该（key存在则修改，key不存在则新增）
my_dict['name'] = '崔某某'
my_dict['addr'] = '黄冈市'
print("修改后的字典：", my_dict)
print(my_dict.setdefault('www', '啊啊啊'))   # key存在，不修改value值，使用默认值，key不存在则新增

# 字典合并，相同key则覆盖，不同则新增
my_dict.update({'name': '大黄', 'weigh':200})
print(my_dict)

# 删除
# del my_dict['www']  # key存在，正常删除，key不存在则报错
# my_dict.pop('www')  # key存在，正常删除，key不存在则报错
# my_dict.clear()     # 清空字典

# 其他操作
# 统计键值对个数
print(len(my_dict))
# 遍历字典
for i in my_dict.keys():
    print(i, my_dict[i])
print('-------------')
for i in my_dict.values():
    print(i)
print('-------------')
for k, v in my_dict.items():
    print(k, v)

dict = {'one': 1, 'two': 2}
print(1 in dict)
print(1 in dict.keys())
print(1 in dict.values())
