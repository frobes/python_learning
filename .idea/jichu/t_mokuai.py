"""
ģ�飺
sysģ��
.pyc�ļ�
from...import���
ģ���_name_
�������Լ���ģ��
dir()����
"""



#sysģ��
import sys 
print r"The common and line arguments are:"

#sys.argv������һ���ַ������б�,�����������в��� ���б���ʹ�������д��ݸ���ĳ���Ĳ�����
for i in sys.argv:
    print i 
#sys.path��������ģ���Ŀ¼���б�  
print '\n\nThe PATH on  PATH is ',sys.path,'\n'






#�ֽڱ����.pyc�ļ�
"""
����һ��ģ�������˵��һ���ȽϷ�ʱ�����飬����Python����һЩ���ɣ��Ա�ʹ����ģ����ӿ�һЩ��һ�ַ����Ǵ��� �ֽڱ�����ļ� ����Щ�ļ���.pyc��Ϊ��չ����
�ֽڱ�����ļ���Python�任������м�״̬�йأ��Ƿ񻹼ǵ�Python��ι����Ľ��ܣ������������´δӱ�ĳ����������ģ���ʱ��.pyc�ļ����ö࣬��Ϊһ����
����ģ������Ĵ����Ѿ�����ˡ����⣬��Щ�ֽڱ�����ļ�Ҳ����ƽ̨�޹صġ�
"""



#from..import���
"""
�������Ҫֱ������argv��������ĳ����У�������ÿ��ʹ����ʱ��sys.������ô�����ʹ��
from sys import argv��䡣�������Ҫ��������sysģ��ʹ�õ����֣���ô�����ʹ��from sys
import *��䡣
"""



#ģ���_name_

# -*- coding:utf-8 -*-
#ÿ��Pythonģ�鶼������__name__���������'__main__'����˵�����ģ�鱻�û���������
"""
if _name_=='_main_':
    print r"This program is being run by itself!"
else:
    print r"I'm being imported from another module"
"""
    
    

#�������Լ���ģ��
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





#dir()����
"""
ʹ���ڽ���dir�������г�ģ�鶨��ı�ʶ������ʶ���к�������ͱ�����
����Ϊdir()�ṩһ��ģ������ʱ��������ģ�鶨��������б�������ṩ�����������ص�ǰģ���ж���������б�
"""

import sys
dir(sys)
dir()
a=2
dir()
#del�����������к�����ɾ��һ������/���ơ�
del a
dir()



   












