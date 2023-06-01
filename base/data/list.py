# 列表

name_list = ['jack', 'pony', 'dowson', 'allen', 'banchon', 'wesper']
print(name_list)

# 增
name_list.append("wenyun")
print(name_list)
name_list.insert(3, "guorong")
print(name_list)

# 改
name_list[2] = "dowsontang"
print(name_list)

# 查
print(name_list.index("jack"))
# print(name_list.index("123")) -- 不存在会报错

# 删
del name_list[3]
print(name_list)
name_list.remove("wenyun")
print(name_list)

# 切片
name_list = ['jack', 'pony', 'dowson', 'allen', 'banchon', 'wesper', 'wenyun']
# 第三个参数是步长
print(name_list[0:6:2])
print(name_list[4:])
print(name_list[:-2])

# 嵌套
name_list.insert(1, ["chen", 160, 45, 28])
print(name_list)
print(name_list[-7][3])
