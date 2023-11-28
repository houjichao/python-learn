name = "Potato"
b = 100
print("你好%s，你的额度是%d" % (name, b))
# name将替换%s的位置，b将替换%d的位置，字符串后的%用来说明是哪些变量要替换前面的占位符，当只有一个变量的时候，可以省略括号


print("小数: %.2f" % 3.14159)  # %.2f代表保留两位小数
print("小数: %.2f" % 4.5)  # %.2f保留两位小数，不够的位用0补充
print("占位: %3d" % 5)  # %3d代表这个数的宽度为3，不够的话用空格在前面补，如果数的宽度大于3，则正常输出
print("前导0: %05d" % 2)  # %05d代表这个数的宽度为5，不够的话用0在前面补，如果数的宽度大于5，则正常输出

print("你好{0}，你的余额是{1:.2f}".format("Potato", 3.1))
# {0}代表占位符和format里的参数对应，{1:.2f}，冒号后是格式控制，代表保留两位小数

print(format(3.1415, ".2f"))
# 结果是3.14
