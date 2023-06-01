#单行注释

#多行注释

'''
多行注释
'''

"""
多行注释
"""

print("Hello Python")

"""
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")
  
IndentationError: unindent does not match any outer indentation level
"""
if True:
    print ("True")
else:
    print ("False")

"""
多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
"""
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
