a = 10
b = 99
print(f'交换前：a={a},b={b}')

#  1.中间变量法
# temp = a
# a = b
# b = temp
# print(f'交换后：a={a},b={b}')

#  2.计算法
# a = a + b
# b = a - b
# a = a - b

# a = a * b
# b = a / b
# a = a / b
# print(f'交换后：a={a},b={b}')

# 3.元组法
(b, a) = ret = (a, b)
print(type(ret))
print(f'交换后：a={a},b={b}')

