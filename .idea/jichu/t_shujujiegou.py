"""
数据结构：Python中有三种内建的数据结构--列表、元组和字典。
列表
元组
字典
序列
引用
更多字符串内容
"""

#列表：list=>类似于购物列表    可变  =》方括号中用逗号分割的项目
"""
列表是使用对象和类的一个例子。当使用变量i并给它赋值的时候，比如赋整数5，你可以认
为你创建了一个类（类型）int的对象（实例）i。
类也有方法，即仅仅为类而定义地函数。仅仅在你有一个该类的对象的时候，你才可以使用这
些功能。例如，Python为list类提供了append方法，这个方法让你在列表尾添加一个项目。例如
mylist.append('an item')列表mylist中增加那个字符串。
一个类也有域，它是仅仅为类而定义的变量。仅仅在你有一个该类的对象的时候，你才可以使
用这些变量/名称。类也通过点号使用，例如mylist.field。
"""
# -*- coding:utf-8 -*-
#filename:using_list.py
shoplist=['apple','carrot','peer','banana']
print 'I have',len(shoplist),'items to purchase.'

print 'These items are:'

for item in shoplist:
  print item,
#在print语句的结尾使用了一个 逗号 来消除每个print语句自动打印的换行符。

print '\nI also have to buy rice!'
shoplist.append('rice')

print 'my shoplist is now :',shoplist

print 'I will sort mylist now:'
shoplist.sort()
print 'Sorted shoplist is now : ',shoplist

print 'The first item I will buy is:',shoplist[0]

olditem=shoplist[0]

del shoplist[0]
print 'I bought the :',olditem

print 'My shopping list is now :',shoplist


#End of using_list.py




#元组：tuple => 不可变 =》圆括号中用逗号分割的项目
"""
含有0个或1个项目的元组。一个空的元组由一对空的圆括号组成，如myempty = ()。
含有单个元素的元组须在第一个（唯一一个）项目后跟一个逗号，这样Python才能区分元组
和表达式中一个带圆括号的对象。即如果是一个包含项目2的元组的时候，应该指明singleton = (2 , )。
"""

# -*- coding:utf-8 -*-
#filename:using_tuple.py


zoo=('wolf','elephant','penguin')
print r"Number of animal in zoo is :",len(zoo)

new_zoo=('monkey','dolphin',zoo)
print r"Number of animal in new_zoo is",len(new_zoo)


print r"All animals in new zoo are:",new_zoo
print r"Animals  brought from old zoo are:",new_zoo[2]
print r"Last animal brought from old zoo is:",new_zoo[2][2]


#End of using_tuple.py

#元组与打印语句
#filename:print_tuple.py
age=22
name='swarr'
#print '%s is %d years old!' ,%(name,age) => invalid syntax
print '%s is %d years old!' %(name,age)
print 'Why is %s playing with that python?'%name

#End of using_tuple.py




#字典：dict  =>类似于你通过联系人名字查找地址和联系人详细情况的地址簿
"""
键必须是唯一的
只能使用不可变的对象（比如字符串）来作为字典的键，可以把不可变或可变的对象作为字典的值。
键值对在字典中以这样的方式标记：d = {key1 : value1, key2 : value2 }。注意它们的键/值对用冒
号分割，而各个对用逗号分割，所有这些都包括在花括号中。

字典是dict类的实例/对象。
"""

#filename:using_dict.py
ab={'Swaroop':'Swaroop@byteofpython.info',
    'Larry':'Larry@wall.org',
    'Mata':'Mata@ruby-lang.org',
    'Spammer':'Spammer@hotmail.com'
}


print  r"Swaroop's address is %s" %ab['Swaroop']

ab['Guido']='Guido@python.org'

del ab['Spammer']

print '\nThere are %d contacts in the address-book \n '%len(ab)

#使用字典的items方法，来使用字典中的每个键/值对。这会返回一个元组的列表，其中每个元组都包含一对项目——键与对应的值。
for name,address in ab.items():
  print  r"Concact %s at %s" %(name,address)
 
#可以使用in操作符来检验一个键/值对是否存在，或者使用dict类的has_key方法。 
if 'Guido' in ab:
  print  '\nGuido\'s address is %s ' %ab['Guido']
  
  

#序列
"""
列表、元组和字符串都是序列
序列的两个主要特点是索引操作符和切片操作符。索引操作符让我们可以从序列中抓取一个特定项目。
切片操作符能够获取序列的一个切片，即一部分序列。
"""
#filename:seq.py
shoplist = ['apple','mongo','banana','carrot']

print 'Item 0 is :',shoplist[0]
print 'Item 1 is :',shoplist[1]
print 'Item 2 is :',shoplist[2]
print 'Item 3 is :',shoplist[3]
print 'Item -1 is:',shoplist[-1]
print 'Item -2 is:',shoplist[-2]

print '\nItem 1 to 3 is:',shoplist[1:3]
print 'Item 2 to end is:',shoplist[2:]
print 'Item 1 to -1 is:',shoplist[1:-1]
print 'Item start to end is:',shoplist[:]


name = 'swaroop'
print '\ncharacters 1 to 3 is ',name[1:3]
print 'characters 2 to end is',name[2:]
print 'characters 1 to -1 is',name[1:-1]
print 'characters start to end is',name[:]
#End of seq.py


#引用
#filename:reference.py

print r"Simple Assignment"
shoplist=['apple','mongo','carrot','banana']
mylist=shoplist

del shoplist[0]

print r"shoplist is:",shoplist
print r"mylist is:",mylist

print r"Copy by making a full slice"
mylist=shoplist[:]
del mylist[0]

print r"shoplist is:",shoplist
print r"mylist is:",mylist
#End of reference.py


#更多字符串的内容
#filename:str_method.py

name='swaroop'

if name.startswith('swa'):
  print  ' Yes,the string starts with "swa"! '
  
if 'a' in name:
  print ' Yes,it contains the string "a"!  '
  
#find方法用来找出给定字符串在另一个字符串中的位置，或者返回-1以表示找不到子字符串。
if name.find('war')!=-1:
  print  ' Yes,it contains the string "war"!  '
  

delmiter='_*_'
mylist=['Brazil','Russia','India','China']
#str类也有以一个作为分隔符的字符串join序列的项目的整洁的方法，它返回一个生成的大字符串。
print delmiter.join(mylist)
  
#End of str_method.py

