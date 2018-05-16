"""
函数:
函数形参
局部变量
默认参数值
关键参数
return语句
docstrings
"""


#函数定义：函数是重用的程序段

def sayhello():
    print r"Hello World!"

sayhello()



#函数形参
#函数中的参数名称为形参（参数在函数定义的圆括号对内指定，用逗号分割），而调用函数时提供给函数调用的值称为实参。

def t_Max(a,b):
    if a > b:
        print a,r"is bigger than",b
    else:
        print b,r"is bigger than",a

a = int(raw_input("请输入a的值："))
b = int(raw_input("请输入b的值："))
t_Max(a,b)

while a > b:
    print a,b
    b = b+1
else:
    print r"b >= a"
    
    

#局部变量
# -*- coding:utf-8 -*-
def func(x):
    print r"x is " ,x
    x = 20
    print r"change local x is ",x

x = 50
func(x)
print r"x is still ",x



#使用global语句
"""
def funk(y)报错：SyntaxError: name 'y' is local and global ，只能写成funk()
可以使用同一个global语句指定多个全局变量。例如global x, y, z。
"""
def funk():
    global y
    print "引用global后的y"
    
    print r"y is ",y
    y=20
    print r"change local y is ",y

y = 50
funk()
print r"y is still ",y





#默认参数值
"""
默认参数值应该是一个参数，是不可变的
"""

def say(message,time=2):
    print message * time
    
say('hello')
say('hello',5)


#关键参数
"""
如果你的某个函数有许多参数，而你只想指定其中的一部分，那么你可以通过命名来为这些参数赋值--这被称作关键参数
"""


def guanjian(a,b=5,c=3):
    print 'a is ',a,'and b is',b,'and c is ',c
    
guanjian(3,7)
guanjian(25,c=24)
guanjian(c=30,a=100)




#return语句
"""
没有返回值的return语句等价于return None。None是Python中表示没有任何东西的特殊类型。例如，如果一个变量的值为None，可以表示它没有值。
"""
def maxnum(x,y):
    if x > y:
        return x
    else:
        return y
    
maxnum(3,8)



def somefunction():
    pass
#pass语句在Python中表示一个空的语句块。





#DocStrings

def printmax(x,y):
    '''Prints the maximum of two numbers.
    The two values must be integers.  '''
    x = int(x)
    y = int(y)
    
    if x > y :
        print 'x is max value!'
    else:
        print r"y is max value!"
        
printmax(5,8)
#AttributeError: 'function' object has no attribute '_doc_'
print printmax._doc_









    
    
