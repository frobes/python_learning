'''
类与实例相互关联：
类是对象的定义，而实例是“真正的实物”，它存放了类中所定义的对象的具体信息。
'''

#创建一个类
class AddrBookEntry(object):  #类定义
    'address book entry class'
    def __init__(self,nm,ph):  #定义构造器
        self.name=nm       #设置name
        self.phone=ph      #设置phone
        print("created instance for :",self.name)
    def updatePhone(self,newph): #定义方法
        self.phone=newph
        print("updated phone# for :",self.name)

#创建实例
john=AddrBookEntry('John Doe','18825144300') #为John Doe创建实例
jane=AddrBookEntry('Jane Doe','13580487764') #为Jane Doe创建实例

#访问实例属性
print(john)
print(john.name)
print(john.phone)
print(jane)
print(jane.name)
print(jane.phone)

#方法调用
john.updatePhone('111111111')
print("更新john号码为：",john.phone)


#创建子类
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class' #员工地址薄类
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid=id
        self.email=em

    def updateEmail(self,newem):
        self.email=newem
        print("updated email address for :",self.name)
print("-----------------------------------------")

#使用子类
john=EmplAddrBookEntry('John Doe','18825144300',42,'1275758000@qq.com')
print("-----------------------------------------")
print(john)
print(john.name)
print(john.phone)
print(john.email)
john.updatePhone('222222222')
print("更新john号码为：",john.phone)
john.updateEmail('64464222@qq.com')
print("更新john邮件为：",john.email)
