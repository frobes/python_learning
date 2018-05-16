'''
在一个函数内部，局部名称空间代表在函数执行时候定义的所有名字，locals()函数返回的是
包含这些名字的字典，globals()函数会返回函数可访问的全局名字。
'''

def foo():
    print("\ncalling foo...")
    astring='bar'
    anint=42
    print("foo()'s globals:\n",globals().keys())
    print("foo()'s locals:\n",locals().keys())

print("__main__'s globals:\n",globals().keys())
print("__main__'s locals:\n",locals().keys())

foo()
