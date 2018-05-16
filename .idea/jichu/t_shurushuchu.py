#输入输出
'''
文件
储存器
'''


#文件

"""
创建一个file类对象来打开文件，读写文件用file类的read、readline、write方法，对文件的读写能力依赖于在打开文件时指定的模式。
关闭文件用close方法。

"""


#filename:using_file.py


poem='''\
Pragraming is fun when the work is done.
if you wanna make you work also fun:
 use Python!
'''

#创建一个file类的实例。模式可以为读模式（'r'）、写模式（'w'）或追加模式（'a'）。记得加冒号''
f=file('poem.txt','w') #open for writing

f.write(poem) #写入poem到poem.txt

f.close()

f=file('poem.txt')

while True:
    line=f.readline()
    if len(line) == 0:
        break
    print line,
    
f.close()

#End of using_file.py



#储存器pickle
"""
Python提供一个标准的模块，称为pickle。使用它可以在一个文件中储存任何Python对象，之
后又可以把它完整无缺地取出来。这被称为 持久地储存对象。
另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。
"""
#filename:picking.py
#import..as语法
import pickle as p


shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']

f=file(shoplistfile,'w')
#调用储存器模块的dump函数，把对象储存到打开的文件中。这个过程称为储存 。
p.dump(shoplist,f)
f.close()

f=file(shoplistfile)
#使用pickle模块的load函数的返回来取回对象。这个过程称为取储存 。
storelist=p.load(f)
print storelist