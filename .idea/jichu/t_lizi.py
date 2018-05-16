
"""
����x2�ĺ���
"""

def power(x):
    return x * x 

print (power(3))


"""
����n�η�
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
һ�꼶Сѧ��ע��ĺ���
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
Ĭ�ϲ�������ָ�򲻱����

"""
def add_end(L=None):
    '''
    ���д��add_end(L=[])����ʹ��Ĭ�ϲ���������û������END��
    Python�����ڶ����ʱ��Ĭ�ϲ���L��ֵ�ͱ���������ˣ���[]����ΪĬ�ϲ���LҲ��һ����������ָ�����[]��ÿ�ε��øú�����
    ����ı���L�����ݣ����´ε���ʱ��Ĭ�ϲ��������ݾͱ��ˣ������Ǻ�������ʱ��[]�ˡ�    
    '''    

    if L is None:
        L=[]
    L.append('END')
    return L

print(add_end())
print(add_end())



"""
����a2 + b2 + c2 + ....
"""
#�ɱ�������Ǵ���Ĳ��������ǿɱ�ģ�������1����2�������������������0������*numbers
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum + n * n
    return sum

#������ǿɱ����������������ȷ�������õ�ʱ����Ҫ����װ��һ��list��tuple
#calc([1,2,3])
#calc((1,3,5,7))
#���ÿɱ���������ú����ķ�ʽ���Լ򻯳�����
print(calc(1,2,3))
print(calc(1,3,5,7))




"""
�ؼ��ֲ���
�ɱ����������0�����������������Щ�ɱ�����ں�������ʱ�Զ���װΪһ��tuple��
���ؼ��ֲ���������0������������������Ĳ�������Щ�ؼ��ֲ����ں����ڲ��Զ���װΪһ��dict��
"""
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
    
person('Jack',24,city='Beijing',addr='chaoyang',zipcode=123456)



"""
�����ؼ��ֲ��������ƹؼ��ֲ���������
�����ؼ��ֲ�����Ҫһ������ָ���*��*����Ĳ�������Ϊ�����ؼ��ֲ���
ֻ����city��job��Ϊ�ؼ��ֲ���
�����ؼ��ֲ�������ʱ���봫�������
"""
#def per(name,age,*,city,job):
#    print(name,age,city,job)
    
#per('Jack',24,city='Beijing',job='Engineer')
    
#invalid syntax: t_lizi.py, line 102, pos 19


"""
�������
���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ�����
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


#*args�ǿɱ������args���յ���һ��tuple��
#**kw�ǹؼ��ֲ�����kw���յ���һ��dict��


"""
�ݹ麯��
�׳�n! = 1 x 2 x 3 x ... x n
"""
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(1))
print(fact(100))
        
#ʹ�õݹ麯����Ҫע���ֹջ������ڼ�����У�����������ͨ��ջ��stack���������ݽṹʵ�ֵģ�ÿ������һ���������ã�
#ջ�ͻ��һ��ջ֡��ÿ���������أ�ջ�ͻ��һ��ջ֡������ջ�Ĵ�С�������޵ģ����ԣ��ݹ���õĴ������࣬�ᵼ��ջ�����
#��fact(1000)
#fact(1000)
#File "e:\project\t_lizi.py", line 148, in fact
#  return n*fact(n-1)
#RuntimeError: maximum recursion depth exceeded

"""
����ݹ����ջ����ķ�����ͨ��β�ݹ��Ż�
β�ݹ���ָ���ں������ص�ʱ�򣬵������������ң�return��䲻�ܰ������ʽ�����������������߽������Ϳ��԰�β�ݹ����Ż���
ʹ�ݹ鱾�����۵��ö��ٴΣ���ֻռ��һ��ջ֡���������ջ����������
"""
def fact2(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact2(5))
#print(fact2(1000)) ���Ǳ���

"""
��ŵ�����ƶ�:
��дmove(n, a, b, c)�����������ղ���n����ʾ3������A��B��C�е�1������A������������Ȼ���ӡ������������
��A����B�ƶ���C�ķ���
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
��Ƭ
"""
L=list(range(100))
print(L[:10])


"""
Python�У�������ͨ��for ... in����ɵ�
Ĭ������£�dict��������key�����Ҫ����value��������for value in d.values()�����Ҫͬʱ����key��value��
������for k, v in d.items()��
"""

d={'a':1,'b':2,'c':3}
for key in d:
    print key
for value in d.values():
    print value
for k,v in d.items():
    print k,v
    
"""
ͨ��collectionsģ���Iterable�����ж�һ�������Ƿ�ɵ�������
"""
from collections import Iterable
if isinstance('abc',Iterable):
    print '�ַ����ɵ���'
if isinstance([1,2,3],Iterable):
    print '�б�ɵ���'


"""
�б�����ʽ
"""
[x * x for x in range(1,11)]

[x * x for x in range(1,11) if x % 2 == 0 ]

[m + n for m in 'ABC' for n in 'XYZ']


import os 
#os.listdir�����г��ļ���Ŀ¼
[d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }
h=[k + '=' + v for k,v in d.items()]
print h



"""
������generator����ѭ���Ĺ����в��������������Ԫ��

"""
L=[x * x for x in range(10)]
g=(x * x for x in range(10))
#L��һ��list����g��һ��generator
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#generator��������㷨��ÿ�ε���next(g)���ͼ����g����һ��Ԫ�ص�ֵ��ֱ�����㵽���һ��Ԫ�أ�û�и����Ԫ��ʱ��
#�׳�StopIteration�Ĵ���
for n in g:
    print n


"""
쳲��������У�Fibonacci��������һ���͵ڶ������⣬����һ����������ǰ��������ӵõ���

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

#fib����������쳲��������е�������򣬿��Դӵ�һ��Ԫ�ؿ�ʼ����������������Ԫ�أ������߼�����generator��
def fib2(max):
    n,a,b=0,0,1
    while n < max:
#���һ�����������а���yield�ؼ��֣���ô��������Ͳ�����һ����ͨ����������һ��generator��
        yield b
        a,b=b,a+b
        n=n+1
#    return 'done'
#SyntaxError: 'return' with argument inside generator (t_lizi.py, line 283)

print fib2(6)
#generator�ͺ�����ִ�����̲�һ����������˳��ִ�У�����return���������һ�к������ͷ��ء������generator�ĺ�����
#��ÿ�ε���next()��ʱ��ִ�У�����yield��䷵�أ��ٴ�ִ��ʱ���ϴη��ص�yield��䴦����ִ�С�

def odd():
    print('step1')
    yield 1
    print('step2')
    yield(3)
    print('step3')
    yield(5)    

#���ø�generatorʱ������Ҫ����һ��generator����Ȼ����next()�������ϻ����һ������ֵ

o=odd()
print(next(o))
print(next(o))
print(next(o))









