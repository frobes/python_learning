"""
֮ǰ�ĳ����ж��Ǹ��ݲ������ݵĺ�������������Ƴ���ġ��ⱻ��Ϊ������̵ı�̡�
����һ�ְ����ݺ͹��ܽ���������ó�Ϊ����Ķ�������������֯����ķ��������ַ�����Ϊ�������ı�����
��Ͷ�������������̵�������Ҫ���档�ഴ��һ�������ͣ�������������ʵ����������������һ��int���͵ı�������洢�����ı�����int���ʵ�������󣩡�

�������ʹ����ͨ�����ڶ���ı����洢���ݡ�����һ���������ı�������Ϊ��
����Ҳ����ʹ��������ĺ��������й��ܡ������ĺ�������Ϊ��ķ�����
��ͷ������Ժϳ�Ϊ������ԡ�
������������--����ÿ��ʵ��/��Ķ���������౾�����Ƿֱ𱻳�Ϊʵ���������������
��ʹ��class�ؼ��ִ����������ͷ���������һ���������С�

self 
��
����ķ���
_init_����
�������ķ���
�̳�
"""

#self
"""
��ķ�������ͨ�ĺ���ֻ��һ���ر������--���Ǳ�����һ������ĵ�һ���������ƣ�����
�ڵ������������ʱ���㲻Ϊ���������ֵ��Python���ṩ���ֵ������ر�ı���ָ����
�����չ�������������self��

Python��θ�self��ֵ�Լ�Ϊ���㲻��Ҫ������ֵ��
��������һ�����ΪMyClass��������һ��ʵ��MyObject����������������ķ���MyObject.method(arg1,arg2)��ʱ��
�����Python�Զ�תΪMyClass.method(MyObject,arg1,arg2)--�����self��ԭ���ˡ�
"""

#��
#filename:simplestclass.py

class Person:
    pass

#ʹ���������һ��Բ����������һ������/ʵ����
p=Person()
print p
#���<__main__.Person instance at 0x0000000002FDF3C8>����__main__ģ��������һ��Person���ʵ����

#����ķ���
#filename:method.py
class Person:
#ע��sayHi����û���κβ���������Ȼ�ں�������ʱ��self��
    def sayhi(self):
        print r"hello,how are you!"
        
p=Person()
p.sayhi()

#End of method.py





#_init_����
"""
__init__���������һ�����󱻽���ʱ���������С�(��ʼ��)
"""

#filename:class_init.py
class Person2:
    #��__init__��������Ϊȡһ������name���Լ���ͨ�Ĳ���self���������__init__�ֻ�Ǵ���һ���µ���Ҳ��Ϊname��
    #ע��������������ͬ�ı�����������������ͬ�����֡����ʹ�����ܹ��������ǡ�
    def __init__(self,name):
        self.name=name
        print r"��ʼ��������",self.name
        
    def __del__(self):
        print r"��ʼ��ɾ��"
        
    def sayhi(self):
        print r"Hello,my name is:",self.name
        
# line 73, in <module>  h = Person2('swaro')TypeError: this constructor takes no arguments
#h = Person2('swaroop')   
#ԭ����python�й��캯����д��ʽ��__init__��������_init_������init���඼��˫�»��ߣ����ǵ��»��ߡ�

h=Person2('swaroop')

h.sayhi()

#End of class_init.py


#�������ķ���
"""
���������͵� �� ������ı����Ͷ���ı��������Ǹ������໹�Ƕ��� ӵ�� ������������֡�
��ı��� ��һ��������ж���ʵ��������ʹ�á�ֻ��һ��������Ŀ��������Ե�ĳ������
����ı������˸Ķ���ʱ������Ķ��ᷴӳ������������ʵ���ϡ�
����ı��� �����ÿ������/ʵ��ӵ�С����ÿ���������Լ���������һ�ݿ����������ǲ�
�ǹ���ģ���ͬһ����Ĳ�ͬʵ���У���Ȼ����ı�������ͬ�����ƣ������ǻ�����صġ�
"""

#filename:objvar.py

class Person3:
    '''Represents a person.'''
    population=0
    
    #population=0
    #Debugger: Debug process paused; pid=6860 [1 modules loaded]:���Թ�����ͣ��PID = 6860 [������1��ģ��]

#population����Person�࣬�����һ����ı�����name�������ڶ�����ʹ��self��ֵ������Ƕ���ı�����   
    def __init__(self,name):
        '''Initalizes the person's data '''
        self.name=name
        print('Inializing %s')%self.name
        
        Person3.population+=1

#��ͬ__init__����һ��������һ������ķ���__del__�����ڶ������ŵ�ʱ�򱻵��á��������ż������ٱ�ʹ�ã�����ռ�õ��ڴ潫���ظ�ϵͳ�����á�
#�������������ֻ�Ǽ򵥵ذ�Person.population��1�� 
#�������ٱ�ʹ��ʱ��__del__�������У����Ǻ��ѱ�֤������������� ʲôʱ�����С������Ҫָ���������У��͵�ʹ��del���
    def __del__(self):
        '''I am dying...'''
        print '%s say goodbye!'%self
        
        Person3.population-=1
        
        if Person3.population == 0:
            print r"I am the last one."
        else:
            print "There are still %d person left."%Person3.population
            
    def sayhi(self):
        '''Greeting by the person;
        Really, that's all it does'''
        
        
        print 'Hi,my name is %s'%self.name
        
    def howmany(self):
        '''print the current population.'''
        
        if Person3.population == 1:
            print r"I'am the only person here!"
        else:
            print r"We have %d person here."%Person3.population
            
swaroop = Person3('swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam = Person3('kalam')
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()

print r"��һ���ĵ��ַ���Ч����"

print Person3._doc_
print Person3.sayhi.__doc__

if __name__ == '__main__':  
    print 'this program is being run by itself.'
    
    
else: 
    print 'I am being imported from other module'  
    
"""
Python�����е����Ա���������ݳ�Ա�����ǹ����ģ����еķ���������Ч�ġ�
ֻ��һ�����⣺�����ʹ�õ����ݳ�Ա������ ˫�»���ǰ׺ ����__privatevar��Python������
������ϵ����Ч�ذ�����Ϊ˽�б�����
"""
#End of objvar.py


#�̳�
"""
�������ı�̴�������Ҫ�ô�֮һ�Ǵ�������ã�ʵ���������õķ���֮һ��ͨ���̳л��ơ��̳���ȫ����������֮��� ���ͺ������� ��ϵ��
"""
#inherit.py

class Schoolmember:
    '''Represents any schoolmember!'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print r"Initalizing school member:%s"%self.name
        
    def tell(self):
        '''Tell my details:'''
        
        print  'Name:"%s";age:"%d"'%(self.name,self.age),

#�̳�:�ѻ������������Ϊһ��Ԫ����ڶ�����ʱ��������֮��
class Teacher(Schoolmember):
    '''Represents a teacher!'''
    def __init__(self,name,age,salary):
        #�������__init__����ר��ʹ��self��������,��ʼ������Ļ����ಿ��
        Schoolmember.__init__(self, name, age)
        self.salary=salary
        print 'Initalizing Teacher:%s'%self.name
        
    def tell(self):
        Schoolmember.tell(self)
        print 'Salary:"%d"'%self.salary
        
class Student(Schoolmember):
    '''Represents a student!'''
    def __init__(self, name,age,marks):
        Schoolmember.__init__(self, name, age)
        self.marks=marks
        print 'Initalizing Student:%s'%self.name
        
    def tell(self):
        Schoolmember.tell(self)
        print 'Mark:"%d"'%self.marks
        

t=Teacher('Mrs.shriv',40,30000)
s=Student('swaroop',22,75)

print #prints a blank line

members=[t,s]

for member in  members:
    member.tell()
    
#End of inherit.py




