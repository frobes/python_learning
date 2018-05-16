
"""
计算x2的函数
"""

def power(x):
    return x * x 

print (power(3))


"""
任意n次方
"""

def power(x,n=2):
    s=1
    while n > 0:
        n = n - 1
        s=s * x  
    return s
        
d = power(3,3)
print d


"""
一年级小学生注册的函数
"""
def enroll(name,gender,age=5,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
    
enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Adm','M',city='Tianjin')


"""
默认参数必须指向不变对象

"""
def add_end(L=None):
    '''
    如果写成add_end(L=[])，则使用默认参数多出调用会输错多个END。
    Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
    如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。    
    '''    

    if L is None:
        L=[]
    L.append('END')
    return L

print(add_end())
print(add_end())



"""
计算a2 + b2 + c2 + ....
"""
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。如*numbers
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum + n * n
    return sum

#如果不是可变参数，参数个数不确定，调用的时候，需要先组装出一个list或tuple
#calc([1,2,3])
#calc((1,3,5,7))
#利用可变参数，调用函数的方式可以简化成这样
print(calc(1,2,3))
print(calc(1,3,5,7))




"""
关键字参数
可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
"""
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
    
person('Jack',24,city='Beijing',addr='chaoyang',zipcode=123456)



"""
命名关键字参数：限制关键字参数的名字
命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
只接收city和job作为关键字参数
命名关键字参数调用时必须传入参数名
"""
#def per(name,age,*,city,job):
#    print(name,age,city,job)
    
#per('Jack',24,city='Beijing',job='Engineer')
    
#invalid syntax: t_lizi.py, line 102, pos 19


"""
参数组合
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""
def f1(a,b,c=0,*args,**kw):
     print('a =', a, 'b =', b, 'c =', c, 'args =',args, 'kw =', kw)
     
#def f2(a,b,c=0,*,d,**kw):
#    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)

f1(1, 2, c=3)

f1(1, 2, 3, 'a', 'b')

f1(1, 2, 3, 'a', 'b', x=99)

#f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。


"""
递归函数
阶乘n! = 1 x 2 x 3 x ... x n
"""
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(1))
print(fact(100))
        
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
#栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#如fact(1000)
#fact(1000)
#File "e:\project\t_lizi.py", line 148, in fact
#  return n*fact(n-1)
#RuntimeError: maximum recursion depth exceeded

"""
解决递归调用栈溢出的方法是通过尾递归优化
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
"""
def fact2(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact2(5))
#print(fact2(1000)) 还是报错

"""
汉诺塔的移动:
编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子
从A借助B移动到C的方法
"""
def move(n,a,b,c):
    if n == 1:
        print('move',a,'--->',c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
        
print(move(4, 'A', 'B', 'C'))


"""
切片
"""
L=list(range(100))
print(L[:10])


"""
Python中，迭代是通过for ... in来完成的
默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，
可以用for k, v in d.items()。
"""

d={'a':1,'b':2,'c':3}
for key in d:
    print key
for value in d.values():
    print value
for k,v in d.items():
    print k,v
    
"""
通过collections模块的Iterable类型判断一个对象是否可迭代对象
"""
from collections import Iterable
if isinstance('abc',Iterable):
    print '字符串可迭代'
if isinstance([1,2,3],Iterable):
    print '列表可迭代'


"""
列表生成式
"""
[x * x for x in range(1,11)]

[x * x for x in range(1,11) if x % 2 == 0 ]

[m + n for m in 'ABC' for n in 'XYZ']


import os 
#os.listdir可以列出文件和目录
[d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }
h=[k + '=' + v for k,v in d.items()]
print h



"""
生成器generator：在循环的过程中不断推算出后续的元素

"""
L=[x * x for x in range(10)]
g=(x * x for x in range(10))
#L是一个list，而g是一个generator
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，
#抛出StopIteration的错误。
for n in g:
    print n


"""
斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""
def fib(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

print fib(6)

#fib函数定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑类似generator。
def fib2(max):
    n,a,b=0,0,1
    while n < max:
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
        yield b
        a,b=b,a+b
        n=n+1
#    return 'done'
#SyntaxError: 'return' with argument inside generator (t_lizi.py, line 283)

print fib2(6)
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
#在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step1')
    yield 1
    print('step2')
    yield(3)
    print('step3')
    yield(5)    

#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值

o=odd()
print(next(o))
print(next(o))
print(next(o))









