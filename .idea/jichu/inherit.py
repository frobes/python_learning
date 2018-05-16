
class Schoolmember:
    '''Represents any schoolmember!'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print r"Initalizing school member:%s"%self.name
		
        
    def tell(self):
        '''Tell my details:'''
        
        print  'Name:"%s";age:"%d"'%(self.name,self.age),

class Teacher(Schoolmember):
    '''Represents a teacher!'''
    def __init__(self,name,age,salary):
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

print Schoolmember.__doc__

members=[t,s]

for member in  members:
    member.tell()
    
#End of inherit.py