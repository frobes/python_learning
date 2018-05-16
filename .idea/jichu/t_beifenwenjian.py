"""
���һ�������ļ��ĳ���
1. ��Ҫ���ݵ��ļ���Ŀ¼��һ���б�ָ����
2. ����Ӧ�ñ�����������Ŀ¼�С�
3. �ļ����ݳ�һ��zip�ļ���
4. zip�浵�������ǵ�ǰ�����ں�ʱ�䡣
5. ����ʹ�ñ�׼��zip�����ͨ��Ĭ�ϵ���Linux/Unix���а��ṩ��Windows�û�����ʹ
��Info-Zip����

"""

#filename:backup_verl.py

import os
import time


#��source�б���ָ����Ҫ���ݵ��ļ���Ŀ¼��
source=['/home/swaroop/byte','/home/swaroop/bin']

#Ŀ��Ŀ¼��Ҫ�洢�����ļ��ĵط�������target_dir����ָ����
target_dir='/mnt/e/backup'

#zip�鵵��������Ŀǰ�����ں�ʱ�䣬ʹ��time.strftime()������á���������.zip��չ��������������target_dirĿ¼�С�
#ʹ�üӷ��������� ���� �ַ��������������ַ���������һ�𷵻�һ���µ��ַ�����
target=target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr'%s'%s "%(target,''.join(source))

#ʹ��os.system���� ���� ���������������ͺ����� ϵͳ ����������һ��������shell������������������ɹ����У�������0�����������ش����
if os.system(zip_command) == 0:
    print r"Successful backup to ",target
else:
    print r"Bacckup failed!"
    
    
#End of backup_verl.py


"""
�Ż���
���ø��õ��ļ�������--ʹ�� ʱ�� ��Ϊ�ļ���������ǰ��������ΪĿ¼���������������Ŀ¼�С���������һ����������ı��ݻ��Եȼ��ṹ�洢��������͸�����
�׹����ˡ�����һ���������ļ����ĳ���Ҳ���Ա�̡�����һ�������ǲ��ø��Զ������ļ��п��԰����㷽��ؼ������Ƿ���ÿһ�촴���˱��ݣ���Ϊֻ�����㴴���˱��ݣ�
�Ż���������Ŀ¼��
"""

#filename :backup_verl2.py

import os
import time

source=['/home/swaroop/byte','/home/swaroop/bin']

target_dir='/mnt/e/backup'


today=target_dir + time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

#ʹ��os.exists����������������Ŀ¼���Ƿ����Ե�ǰ������Ϊ���Ƶ�Ŀ¼�����û��,ʹ��os.mkdir��������
if not os.path.exists(today):
   os.mkdir(today)
   print r"Successfully created directory",today

#ע��os.sep�������÷�������������Ĳ���ϵͳ����Ŀ¼�ָ���������Linux��Unix������'/'����Windows������'\\'������Mac OS������':'��
##ʹ��os.sep����ֱ��ʹ���ַ�����ʹ���������ֲ�ԣ�������������Щϵͳ�¹�����    
target=today+os.sep + now +'.zip'

zip_command="zip -qr'%s'%s"%(target,''.join(source))

if os.system(zip_command) == 0:
    print r"successful backup to ",target
else:
    print r"Backup Failed!"
    
    

# End of backup_verl2.py

"""
����м��౸�ݵ�ʱ��Ҫ����ÿ�������Ǹ�ʲô�ģ�����ʮ�����ѣ����磬�ҿ��ܶԳ�������ݽ�������һЩ��Ҫ�ĸ�
�䣬��������Ҫ����Щ�ı���zip�鵵��������ϵ�����������ͨ����zip�鵵���ϸ���һ���û��ṩ��ע���������ʵ�֡�
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
