import keyword

# 输出所有python关键字
print(keyword.kwlist)

print("===================")

# 判断字符串是否为关键字
while True:
    str = input()
    if str in keyword.kwlist:
        print(f'{str}是关键字')
    else:
        print(f'{str}不是关键字')
