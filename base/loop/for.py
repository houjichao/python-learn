for letter in 'Python':
    print("当前字母 %s" % letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('当前水果：%s' % fruit)

# 通过序列索引迭代
for index in range(len(fruits)):
    print('当前水果：%s' % fruits[index])

# 循环使用else语句
for num in range(10, 20):
    for i in range(2, num):
        if (num % 2) == 0:
            j = num / i
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:
        print('%d 是一个质数' % num)
