#异常
"""
try...except
引发异常
try...finally
"""

#try..except
#filename:try_except.py

import sys
#把所有可能引发错误的语句放在try块中，然后在except从句/块中处理所有的错误和异常。
#except从句可以专门处理单一的错误或异常，或者一组包括在圆括号内的错误/异常。
try:
    s=raw_input('Enter something:')
except EOFError:
    print'\nWhy did you do an EOF on me!'
    sys.exit()
except:
    print '\nSome error/exception occurred!'
    
print 'Done!'
#End of try_except.py


#引发异常：raise
#filename:raising.py

#异常类型是ShortInputException类。它有两个域——length是给定输入的长度，atleast则是程序期望的最小长度。
class ShortInputException(Exception):
    '''A user-defined exception class!'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
        
try:
    s=raw_input('Enter somethin-->')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
        
except EOFError:
    print r"Why did you do an EOF error on me!"
         
except ShortInputException,x:
    print 'ShortInputException:The input was of length"%d",\
    was esception at least "%d""'%(x.length,x.atleast)
    
else:
    print 'No exception was raised!'
    
    

#try...finally
"""
注意，在一个try块下可以同时使用except从句和finally块。如果要同时使用它们的话，需要把一个嵌入另外一个。
"""
#filename:finally.py
import time

try:
    f=file('poem.txt')
    while True:
        line=f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'

  
#在程序运行的时候，按Ctrl-c中断/取消程序,可以观察到KeyboardInterrupt异常被触发，程序退出。但是在程序退出之前，finally从句仍然被执行，把文件关闭   
#End of finally.py
