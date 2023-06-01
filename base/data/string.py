"""
Python 中单引号 ' 和双引号 " 使用完全相同。

"""

"""
字符串特性'
-- 不可修改
-- 有索引，可切片（顾头不顾尾）
"""
name = "houjichao"
print(name)
print(id(name))  # id -- 取地址
name = "jackjchou"
print(name)
print(id(name))

# 切片
print(name[5])
print(name[0:3])

print(name.center(50, "-"))
print(name.upper())

# 多行字符串
msg = """
hello 
my name is xxx
learn python
"""
print(msg)

# 字符串拼接
name = "houjichao"
school = "交大"
print(name + school)

"""
字符串引用外部变量
%s
f
"""
name = "jack"
age = 26
hobby = "game"
msg = '''
------------ %s info ---------------------
name: %s
age: %d
hobby: %s
------------ end ---------------------
''' % (name, name, age, hobby)
print(msg)

fmsg = f'''                                  
------------ {name} info --------------------- 
name: {name}                                   
age: {age}                                    
hobby: {hobby}                                  
------------ f end ---------------------     
'''
print(fmsg)