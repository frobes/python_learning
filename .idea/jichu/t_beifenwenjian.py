"""
设计一个备份文件的程序
1. 需要备份的文件和目录由一个列表指定。
2. 备份应该保存在主备份目录中。
3. 文件备份成一个zip文件。
4. zip存档的名称是当前的日期和时间。
5. 我们使用标准的zip命令，它通常默认地随Linux/Unix发行版提供。Windows用户可以使
用Info-Zip程序。

"""

#filename:backup_verl.py

import os
import time


#在source列表中指定需要备份的文件和目录。
source=['/home/swaroop/byte','/home/swaroop/bin']

#目标目录是要存储备份文件的地方，它由target_dir变量指定。
target_dir='/mnt/e/backup'

#zip归档的名称是目前的日期和时间，使用time.strftime()函数获得。它还包括.zip扩展名，将被保存在target_dir目录中。
#使用加法操作符来 级连 字符串，即把两个字符串连接在一起返回一个新的字符串。
target=target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr'%s'%s "%(target,''.join(source))

#使用os.system函数 运行 命令，利用这个函数就好像在 系统 中运行命令一样。即在shell中运行命令——如果命令成功运行，它返回0，否则它返回错误号
if os.system(zip_command) == 0:
    print r"Successful backup to ",target
else:
    print r"Bacckup failed!"
    
    
#End of backup_verl.py


"""
优化：
采用更好的文件名机制--使用 时间 作为文件名，而当前的日期作为目录名，存放在主备份目录中。这样做的一个优势是你的备份会以等级结构存储，因此它就更加容
易管理了。另外一个优势是文件名的长度也可以变短。还有一个优势是采用各自独立的文件夹可以帮助你方便地检验你是否在每一天创建了备份，因为只有在你创建了备份，
才会出现那天的目录。
"""

#filename :backup_verl2.py

import os
import time

source=['/home/swaroop/byte','/home/swaroop/bin']

target_dir='/mnt/e/backup'


today=target_dir + time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

#使用os.exists函数检验在主备份目录中是否有以当前日期作为名称的目录。如果没有,使用os.mkdir函数创建
if not os.path.exists(today):
   os.mkdir(today)
   print r"Successfully created directory",today

#注意os.sep变量的用法——这会根据你的操作系统给出目录分隔符，即在Linux、Unix下它是'/'，在Windows下它是'\\'，而在Mac OS下它是':'。
##使用os.sep而非直接使用字符，会使程序具有移植性，可以在上述这些系统下工作。    
target=today+os.sep + now +'.zip'

zip_command="zip -qr'%s'%s"%(target,''.join(source))

if os.system(zip_command) == 0:
    print r"successful backup to ",target
else:
    print r"Backup Failed!"
    
    

# End of backup_verl2.py

"""
如果有极多备份的时候，要区分每个备份是干什么的，会变得十分困难！例如，我可能对程序或者演讲稿做了一些重要的改
变，于是我想要把这些改变与zip归档的名称联系起来。这可以通过在zip归档名上附带一个用户提供的注释来方便地实现。
"""
#filename:backup_ver3.py
import os
import time
source = ['/home/swaroop/byte', '/home/swaroop/bin']

target_dir = '/mnt/e/backup/' 

today=target_dir + time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=raw_input("Enter comment-->")

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(''.'_') + '.zip'
    

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today
    
zip_command = "zip -qr '%s' %s" % (target, ''.join(source))
   
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'    
    
    
#End of backup_ver3.py
