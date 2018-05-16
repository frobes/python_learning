"""
模块：
sys模块
.pyc文件
from...import语句
模块的_name_
制造你自己的模块
dir()函数
"""



#sys模块
import sys 
print r"The common and line arguments are:"

#sys.argv变量是一个字符串的列表,包含了命令行参数 的列表，即使用命令行传递给你的程序的参数。
for i in sys.argv:
    print i 
#sys.path包含输入模块的目录名列表。  
print '\n\nThe PATH on  PATH is ',sys.path,'\n'






#字节编译的.pyc文件
"""
输入一个模块相对来说是一个比较费时的事情，所以Python做了一些技巧，以便使输入模块更加快一些。一种方法是创建 字节编译的文件 ，这些文件以.pyc作为扩展名。
字节编译的文件与Python变换程序的中间状态有关（是否还记得Python如何工作的介绍？）。当你在下次从别的程序输入这个模块的时候，.pyc文件会快得多，因为一部分
输入模块所需的处理已经完成了。另外，这些字节编译的文件也是与平台无关的。
"""



#from..import语句
"""
如果你想要直接输入argv变量到你的程序中（避免在每次使用它时打sys.），那么你可以使用
from sys import argv语句。如果你想要输入所有sys模块使用的名字，那么你可以使用from sys
import *语句。
"""



#模块的_name_

# -*- coding:utf-8 -*-
#每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行
"""
if _name_=='_main_':
    print r"This program is being run by itself!"
else:
    print r"I'm being imported from another module"
"""
    
    

#制造你自己的模块
# -*- coding:utf-8 -*-
#filename:mymodule.py
def sayhi():
    print r"hi,this is my module speaking..."
    
version='0.1'

#End of mymodule.py


# -*- coding:utf-8 -*-
#filename:mymodule_demo.py
import mymodule
mymodule.sayhi()
print 'Version:',mymodule.version
#End of mymodule_demo.py

# -*- coding:utf-8 -*-
#filename:mymodule_demo2.py
from mymodule import sayhi,version
sayhi()
print 'Version = ' ,version
#End of mymodule_demo2.py





#dir()函数
"""
使用内建的dir函数来列出模块定义的标识符。标识符有函数、类和变量。
当你为dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当前模块中定义的名称列表。
"""

import sys
dir(sys)
dir()
a=2
dir()
#del这个语句在运行后被用来删除一个变量/名称。
del a
dir()



   












