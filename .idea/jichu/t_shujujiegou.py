"""
���ݽṹ��Python���������ڽ������ݽṹ--�б�Ԫ����ֵ䡣
�б�
Ԫ��
�ֵ�
����
����
�����ַ�������
"""

#�б�list=>�����ڹ����б�    �ɱ�  =�����������ö��ŷָ����Ŀ
"""
�б���ʹ�ö�������һ�����ӡ���ʹ�ñ���i��������ֵ��ʱ�򣬱��縳����5���������
Ϊ�㴴����һ���ࣨ���ͣ�int�Ķ���ʵ����i��
��Ҳ�з�����������Ϊ�������غ���������������һ������Ķ����ʱ����ſ���ʹ����
Щ���ܡ����磬PythonΪlist���ṩ��append��������������������б�β���һ����Ŀ������
mylist.append('an item')�б�mylist�������Ǹ��ַ�����
һ����Ҳ�������ǽ���Ϊ�������ı���������������һ������Ķ����ʱ����ſ���ʹ
����Щ����/���ơ���Ҳͨ�����ʹ�ã�����mylist.field��
"""
# -*- coding:utf-8 -*-
#filename:using_list.py
shoplist=['apple','carrot','peer','banana']
print 'I have',len(shoplist),'items to purchase.'

print 'These items are:'

for item in shoplist:
  print item,
#��print���Ľ�βʹ����һ�� ���� ������ÿ��print����Զ���ӡ�Ļ��з���

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




#Ԫ�飺tuple => ���ɱ� =��Բ�������ö��ŷָ����Ŀ
"""
����0����1����Ŀ��Ԫ�顣һ���յ�Ԫ����һ�Կյ�Բ������ɣ���myempty = ()��
���е���Ԫ�ص�Ԫ�����ڵ�һ����Ψһһ������Ŀ���һ�����ţ�����Python��������Ԫ��
�ͱ��ʽ��һ����Բ���ŵĶ��󡣼������һ��������Ŀ2��Ԫ���ʱ��Ӧ��ָ��singleton = (2 , )��
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

#Ԫ�����ӡ���
#filename:print_tuple.py
age=22
name='swarr'
#print '%s is %d years old!' ,%(name,age) => invalid syntax
print '%s is %d years old!' %(name,age)
print 'Why is %s playing with that python?'%name

#End of using_tuple.py




#�ֵ䣺dict  =>��������ͨ����ϵ�����ֲ��ҵ�ַ����ϵ����ϸ����ĵ�ַ��
"""
��������Ψһ��
ֻ��ʹ�ò��ɱ�Ķ��󣨱����ַ���������Ϊ�ֵ�ļ������԰Ѳ��ɱ��ɱ�Ķ�����Ϊ�ֵ��ֵ��
��ֵ�����ֵ����������ķ�ʽ��ǣ�d = {key1 : value1, key2 : value2 }��ע�����ǵļ�/ֵ����ð
�ŷָ���������ö��ŷָ������Щ�������ڻ������С�

�ֵ���dict���ʵ��/����
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

#ʹ���ֵ��items��������ʹ���ֵ��е�ÿ����/ֵ�ԡ���᷵��һ��Ԫ����б�����ÿ��Ԫ�鶼����һ����Ŀ���������Ӧ��ֵ��
for name,address in ab.items():
  print  r"Concact %s at %s" %(name,address)
 
#����ʹ��in������������һ����/ֵ���Ƿ���ڣ�����ʹ��dict���has_key������ 
if 'Guido' in ab:
  print  '\nGuido\'s address is %s ' %ab['Guido']
  
  

#����
"""
�б�Ԫ����ַ�����������
���е�������Ҫ�ص�����������������Ƭ�����������������������ǿ��Դ�������ץȡһ���ض���Ŀ��
��Ƭ�������ܹ���ȡ���е�һ����Ƭ����һ�������С�
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


#����
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


#�����ַ���������
#filename:str_method.py

name='swaroop'

if name.startswith('swa'):
  print  ' Yes,the string starts with "swa"! '
  
if 'a' in name:
  print ' Yes,it contains the string "a"!  '
  
#find���������ҳ������ַ�������һ���ַ����е�λ�ã����߷���-1�Ա�ʾ�Ҳ������ַ�����
if name.find('war')!=-1:
  print  ' Yes,it contains the string "war"!  '
  

delmiter='_*_'
mylist=['Brazil','Russia','India','China']
#str��Ҳ����һ����Ϊ�ָ������ַ���join���е���Ŀ������ķ�����������һ�����ɵĴ��ַ�����
print delmiter.join(mylist)
  
#End of str_method.py

