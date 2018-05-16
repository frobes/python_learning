#上下文管理
'''
with语句语法：
with context_expr[as var]:
    with_suite
'''
#coding=utf-8
with open('abc.txt','r') as f:
    for eachline in f:
        print(eachline)
#这段代码会自动完成准备工作，比如试图打开一个文件，如果一切正常，把文件对象赋值给f,然后用迭代器遍历文件中的每一行，当完成时，关闭文件。
#实际上只进行了两层处理
#1、发生在用户层--和in类似，需关心的只是被使用的对象
#2、发生在对象层--这个对象支持上下文管理协议，所干的也是“上下文管理。”



