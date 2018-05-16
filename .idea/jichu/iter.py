#coding=utf-8
'''
1.序列（迭代器）
for i in seq:
    do_something_to(i)

等价于：

fetch = iter(seq)
while True:
    try:
        i = fetch.next()
    except StopIteration:
        break
    do_something_to(i)

2.字典（迭代）
字典和文件是另外两个可迭代的python数据类型。
字典的迭代器会遍历他的键
for eachkey in myDict.keys()等价于 for eachkey in myDict


3.文件（迭代）
文件对象生成的迭代器会自动调用readline()方法，这样循环就可以访问文本文件的所有行
for eachLine in myFile 等价于 for eachLine in myFile.realines()

'''

'''
列表解析：
[expr for iter_var in iterable if cond_expr]

生成器表达式：
[expr for iter_var in iterable if cond_expr]

'''
