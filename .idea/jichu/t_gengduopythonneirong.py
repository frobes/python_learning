#更多python内容
"""
特殊的方法
单语句块
列表综合
在函数中接收元组和列表
lanbda形式
exec和eval语句
assert语句
repr函数
"""



#特殊的方法
"""
一些特殊的方法
名称 说明
__init__(self,...) 这个方法在新建对象恰好要被返回使用之前被调用。
__del__(self) 恰好在对象要被删除之前调用。
__str__(self) 在我们对对象使用print语句或是使用str()的时候调用。
__lt__(self,other) 当使用 小于 运算符（<）的时候调用。类似地，对于所有的运算符（+，>等等）都有特殊的方法。
__getitem__(self,key) 使用x[key]索引操作符的时候调用。
__len__(self) 对序列对象使用内建的len()函数的时候调用。
"""

#单语句块
#如果语句块只包含一句语句，可以在条件语句或循环语句的同一行指明它。
flag=True
if flag:print 'Yes!'


#列表综合
"""
通过列表综合，可以从一个已有的列表导出一个新的列表。例如，你有一个数的列表，而你想
要得到一个对应的列表，使其中所有大于2的数都是原来的2倍。
"""
listone=[2,3,4]
listtwo=[2 * i for i in listone if i > 2]
print listone
print listtwo




#在函数中接收元组和列表
"""
当要使函数接收元组或字典形式的参数的时候，有一种特殊的方法，它分别使用*和**前缀。
这种方法在函数需要获取可变数量的参数的时候特别有用。
"""
#由于在args变量前有*前缀，所有多余的函数参数都会作为一个元组存储在args中。如果使用的是**前缀，多余的参数则会被认为是一个字典的键/值对。
def powersum(power,*args):
    'Return the sum of each argument raised to specified power!'
    total=0
    for i in args:
        total+=pow(i,power)
    return total

# pow() 方法返回 xy(x的y次方) 的值。

powersum(2,3,4)
#3^2+4^2

powersum(2,10)
#10^2


#lanbda形式:lambda语句被用来创建新的函数对象，并且在运行时返回它们。

#filename:lambda.py
"""
make_repeater函数在运行时创建新的函数对象，并且返回它。
lambda语句用来创建函数对象。本质上，lambda需要一个参数，后面仅跟单个表达式作为函数体，而表达式
的值被这个新建的函数返回。注意，即便是print语句也不能用在lambda形式中，只能使用表达式。
"""
def make_repeater(n):
    return lambda s:s*n

twice=make_repeater(2)
print twice('word')
print twice(5)




#exec和eval语句
"""
exec语句用来执行储存在字符串或文件中的Python语句。
eval语句用来计算存储在字符串中的有效Python表达式。
"""

exec 'print "Hello world!"'

eval('2*3')




#assert语句
"""
assert语句用来声明某个条件是真的。例如，如果你非常确信某个你使用的列表中至少有一个
元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这
种情形下的理想语句。当assert语句失败的时候，会引发一个AssertionError。
"""
>>>mylist=['item']
>>>assert len(mylist) >= 1
>>>mylist.pop()

>>>assert len(mylist) >= 1



#repr函数
"""
repr函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。注
意，在大多数时候有eval(repr(object)) == object。
"""
>>>i = []
>>>i.append('item')
>>>'i'
>>>repr(i)
#基本上，repr函数和反引号用来获取对象的可打印的表示形式。你可以通过定义类的__repr__方法来控制你的对象在被repr函数调用的时候返回的内容。