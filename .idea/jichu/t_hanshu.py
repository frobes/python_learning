"""
����:
�����β�
�ֲ�����
Ĭ�ϲ���ֵ
�ؼ�����
return���
docstrings
"""


#�������壺���������õĳ����

def sayhello():
    print r"Hello World!"

sayhello()



#�����β�
#�����еĲ�������Ϊ�βΣ������ں��������Բ���Ŷ���ָ�����ö��ŷָ�������ú���ʱ�ṩ���������õ�ֵ��Ϊʵ�Ρ�

def t_Max(a,b):
    if a > b:
        print a,r"is bigger than",b
    else:
        print b,r"is bigger than",a

a = int(raw_input("������a��ֵ��"))
b = int(raw_input("������b��ֵ��"))
t_Max(a,b)

while a > b:
    print a,b
    b = b+1
else:
    print r"b >= a"
    
    

#�ֲ�����
# -*- coding:utf-8 -*-
def func(x):
    print r"x is " ,x
    x = 20
    print r"change local x is ",x

x = 50
func(x)
print r"x is still ",x



#ʹ��global���
"""
def funk(y)����SyntaxError: name 'y' is local and global ��ֻ��д��funk()
����ʹ��ͬһ��global���ָ�����ȫ�ֱ���������global x, y, z��
"""
def funk():
    global y
    print "����global���y"
    
    print r"y is ",y
    y=20
    print r"change local y is ",y

y = 50
funk()
print r"y is still ",y





#Ĭ�ϲ���ֵ
"""
Ĭ�ϲ���ֵӦ����һ���������ǲ��ɱ��
"""

def say(message,time=2):
    print message * time
    
say('hello')
say('hello',5)


#�ؼ�����
"""
������ĳ��������������������ֻ��ָ�����е�һ���֣���ô�����ͨ��������Ϊ��Щ������ֵ--�ⱻ�����ؼ�����
"""


def guanjian(a,b=5,c=3):
    print 'a is ',a,'and b is',b,'and c is ',c
    
guanjian(3,7)
guanjian(25,c=24)
guanjian(c=30,a=100)




#return���
"""
û�з���ֵ��return���ȼ���return None��None��Python�б�ʾû���κζ������������͡����磬���һ��������ֵΪNone�����Ա�ʾ��û��ֵ��
"""
def maxnum(x,y):
    if x > y:
        return x
    else:
        return y
    
maxnum(3,8)



def somefunction():
    pass
#pass�����Python�б�ʾһ���յ����顣





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









    
    
