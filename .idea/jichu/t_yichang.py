#�쳣
"""
try...except
�����쳣
try...finally
"""

#try..except
#filename:try_except.py

import sys
#�����п������������������try���У�Ȼ����except�Ӿ�/���д������еĴ�����쳣��
#except�Ӿ����ר�Ŵ���һ�Ĵ�����쳣������һ�������Բ�����ڵĴ���/�쳣��
try:
    s=raw_input('Enter something:')
except EOFError:
    print'\nWhy did you do an EOF on me!'
    sys.exit()
except:
    print '\nSome error/exception occurred!'
    
print 'Done!'
#End of try_except.py


#�����쳣��raise
#filename:raising.py

#�쳣������ShortInputException�ࡣ���������򡪡�length�Ǹ�������ĳ��ȣ�atleast���ǳ�����������С���ȡ�
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
ע�⣬��һ��try���¿���ͬʱʹ��except�Ӿ��finally�顣���Ҫͬʱʹ�����ǵĻ�����Ҫ��һ��Ƕ������һ����
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

  
#�ڳ������е�ʱ�򣬰�Ctrl-c�ж�/ȡ������,���Թ۲쵽KeyboardInterrupt�쳣�������������˳��������ڳ����˳�֮ǰ��finally�Ӿ���Ȼ��ִ�У����ļ��ر�   
#End of finally.py
