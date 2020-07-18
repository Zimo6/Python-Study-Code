"""
常见数据类型分类
【数字型】：  整型(int)、浮点型(float)、布尔型(Boolean)         复数型(complex了解)
【非数字型】：字符串(str)、列表(list)、元组(tuple)、字典(dict)   集合(了解)
"""
value = 12.3
value1 = "a"
value2 = ["hello"]
value3 = ("aaa", 123)
value4 = {"name": "dog"}
# 数据类型检测
print(type(value))

# Python可以进行类型转换：自动转换、强制转换
# 【列表和元祖可以互转，数字类型的字符串也可以转为整数或者浮点数】
num1 = 100
num2 = 100.123
print(float(num1))
print(int(num2))
print(num1 + num2)  # 进行了自动转换

# Python字符串
str1 = '崔双麒'
str2 = "崔双'麒'"      # 字符串嵌套
str3 = "崔\'双'麒\\"   # 字符串转义
str4 = """  awa
崔双麒
            haha
a
"""
print(str1)
print(str2)
print(str3)
print(str4)
