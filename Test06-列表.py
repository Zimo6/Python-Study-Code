# 【列表】
# 用于存放多个数据的高级容器（有序）
# 定义
my_list1 = [100, 12.3, True, 'hello']
my_list2 = list()  # 面向对象方式
info_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(info_list)

print('=========分割线==========')

# 1、列表常见操作
print("原来的列表：", info_list)
# 1.1 访问数据(通过索引，注意索引越界)
print(info_list[2])
# 1.2 插入数据
info_list.insert(0, 100)              # 在0索引处插入
info_list.insert(2, ['嘻嘻', '哈哈'])  # 在0索引处插入
info_list.append('崔双麒')             # 在末尾插入
print("插入后的列表", info_list)
# 1.3 删除数据
del info_list[0]                 #删除指定索引的数据
info_list.remove('崔双麒')       #删除第一次出现的指定数据（常用）
info_list.pop()                  #删除末尾数据    （返回值为末尾数据）
info_list.pop(0)                 #删除指定索引数据（返回值为删除的数据）
# info_list.clear()               #清空列表
print("删除后的列表", info_list)
# 1.4 修改数据
info_list[0][1] = '崔崔'      # 修改指定索引的数据
info_list[4] = 500            # 修改指定索引的数据
print("修改后的列表", info_list)

print('=========分割线==========')

# 2、列表高级操作
# 2.1 统计列表长度（列表元素个数）
print(len(info_list))
# 2.2 数据在列表中出现的次数
print(info_list.count(500))     # 没有数据则返回0
# 2.3 列表排序
list1 = [15, 15641, 1.1, 5, 45]
list1.sort()                    # 升序（从小到大）
list1.sort(reverse= True)       # 升序（从小到大）
print("升序后的list1", list1)
list1.reverse()                 # 逆序、反转
print("逆序后的list1", list1)
# 2.4 列表拷贝
new_list1 = list1.copy()
print("拷贝后的列表：", new_list1)
# 2.5 合并列表
new_list2 = list1.extend(new_list1)
print(new_list2)
# 2.6 列表切片
print(list1[0:1])
print(list1[::-1])

# 遍历列表
for i in range(0, len(list1)):
    print(list1[i])

# ***列表推导式：快速创建列表***
a_list = [x for x in range(10)]
b_list = [x for x in range(1, 10, 2)]
print(a_list)
print(b_list)