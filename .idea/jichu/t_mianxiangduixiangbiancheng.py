"""
之前的程序中都是根据操作数据的函数或语句块来设计程序的。这被称为面向过程的编程。
还有一种把数据和功能结合起来，用称为对象的东西包裹起来组织程序的方法。这种方法称为面向对象的编程理念。
类和对象是面向对象编程的两个主要方面。类创建一个新类型，而对象这个类的实例。这类似于你有一个int类型的变量，这存储整数的变量是int类的实例（对象）。

对象可以使用普通的属于对象的变量存储数据。属于一个对象或类的变量被称为域。
对象也可以使用属于类的函数来具有功能。这样的函数被称为类的方法。
域和方法可以合称为类的属性。
域有两种类型--属于每个实例/类的对象或属于类本身。它们分别被称为实例变量和类变量。
类使用class关键字创建。类的域和方法被列在一个缩进块中。

self 
类
对象的方法
_init_方法
类与对象的方法
继承
"""

#self
"""
类的方法与普通的函数只有一个特别的区别--它们必须有一个额外的第一个参数名称，但是
在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本
身，按照惯例它的名称是self。

Python如何给self赋值以及为何你不需要给它赋值？
假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法MyObject.method(arg1,arg2)的时候，
这会由Python自动转为MyClass.method(MyObject,arg1,arg2)--这就是self的原理了。
"""

#类
#filename:simplestclass.py

class Person:
    pass

#使用类名后跟一对圆括号来创建一个对象/实例。
p=Person()
print p
#输出<__main__.Person instance at 0x0000000002FDF3C8>：在__main__模块中有了一个Person类的实例。

#对象的方法
#filename:method.py
class Person:
#注意sayHi方法没有任何参数，但仍然在函数定义时有self。
    def sayhi(self):
        print r"hello,how are you!"
        
p=Person()
p.sayhi()

#End of method.py





#_init_方法
"""
__init__方法在类的一个对象被建立时，马上运行。(初始化)
"""

#filename:class_init.py
class Person2:
    #把__init__方法定义为取一个参数name（以及普通的参数self）。在这个__init__里，只是创建一个新的域，也称为name。
    #注意它们是两个不同的变量，尽管它们有相同的名字。点号使我们能够区分它们。
    def __init__(self,name):
        self.name=name
        print r"初始化参数：",self.name
        
    def __del__(self):
        print r"初始化删除"
        
    def sayhi(self):
        print r"Hello,my name is:",self.name
        
# line 73, in <module>  h = Person2('swaro')TypeError: this constructor takes no arguments
#h = Person2('swaroop')   
#原因：在python中构造函数书写格式是__init__，而不是_init_，即在init两侧都是双下划线，不是单下划线。

h=Person2('swaroop')

h.sayhi()

#End of class_init.py


#类与对象的方法
"""
有两种类型的 域 ——类的变量和对象的变量，它们根据是类还是对象 拥有 这个变量而区分。
类的变量 由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以当某个对象
对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
对象的变量 由类的每个对象/实例拥有。因此每个对象有自己对这个域的一份拷贝，即它们不
是共享的，在同一个类的不同实例中，虽然对象的变量有相同的名称，但是是互不相关的。
"""

#filename:objvar.py

class Person3:
    '''Represents a person.'''
    population=0
    
    #population=0
    #Debugger: Debug process paused; pid=6860 [1 modules loaded]:调试过程暂停；PID = 6860 [加载了1个模块]

#population属于Person类，因此是一个类的变量。name变量属于对象（它使用self赋值）因此是对象的变量。   
    def __init__(self,name):
        '''Initalizes the person's data '''
        self.name=name
        print('Inializing %s')%self.name
        
        Person3.population+=1

#如同__init__方法一样，还有一个特殊的方法__del__，它在对象消逝的时候被调用。对象消逝即对象不再被使用，它所占用的内存将返回给系统作它用。
#在这个方法里面只是简单地把Person.population减1。 
#当对象不再被使用时，__del__方法运行，但是很难保证这个方法究竟在 什么时候运行。如果想要指明它的运行，就得使用del语句
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

print r"看一下文档字符串效果："

print Person3._doc_
print Person3.sayhi.__doc__

if __name__ == '__main__':  
    print 'this program is being run by itself.'
    
    
else: 
    print 'I am being imported from other module'  
    
"""
Python中所有的类成员（包括数据成员）都是公共的，所有的方法都是有效的。
只有一个例外：如果你使用的数据成员名称以 双下划线前缀 比如__privatevar，Python的名称
管理体系会有效地把它作为私有变量。
"""
#End of objvar.py


#继承
"""
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的 类型和子类型 关系。
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

#继承:把基本类的名称作为一个元组跟在定义类时的类名称之后
class Teacher(Schoolmember):
    '''Represents a teacher!'''
    def __init__(self,name,age,salary):
        #基本类的__init__方法专门使用self变量调用,初始化对象的基本类部分
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




