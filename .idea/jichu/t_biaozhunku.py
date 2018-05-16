#python��׼��
"""
sysģ��
osģ��
"""


#sys
"""
sys.version�ַ��������ṩ��װ��Python�İ汾��Ϣ��sys.version_infoԪ�����ṩһ�����򵥵�
������ʹ��ĳ���߱�Python�汾Ҫ���ܡ�
"""
#filename:cat.py


import sys
def readfile(filename):
    '''print a file to the standard output!'''
    f=file(filename)
    while True:
        line=f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()
    
    
if len(sys.argv) < 2:
    print 'NO action specified!'
    sys.exit()
    
if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''\
      this program prints files to the standard output.
      Any number of files can be specified!
      Options include:
      --version : Prints the version number
      --help : Display this help
       '''
    else:
        print 'Unknown option!'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
        
#End of cat.py



#os
"""
ʹ��os.sep����ȡ������ϵͳ�ض���·���ָ����
osģ�飺
�� os.name�ַ���ָʾ������ʹ�õ�ƽ̨���������Windows������'nt'��������Linux/Unix�û�������'posix'��
�� os.getcwd()�����õ���ǰ����Ŀ¼������ǰPython�ű�������Ŀ¼·����
�� os.getenv()��os.putenv()�����ֱ�������ȡ�����û���������
�� os.listdir()����ָ��Ŀ¼�µ������ļ���Ŀ¼����
�� os.remove()��������ɾ��һ���ļ���
�� os.system()������������shell���
�� os.linesep�ַ���������ǰƽ̨ʹ�õ�����ֹ�������磬Windowsʹ��'\r\n'��Linuxʹ��'\n'��Macʹ��'\r'��
�� os.path.split()��������һ��·����Ŀ¼�����ļ�����
>>> os.path.split('/home/swaroop/byte/code/poem.txt')
('/home/swaroop/byte/code', 'poem.txt')
�� os.path.isfile()��os.path.isdir()�����ֱ���������·����һ���ļ�����Ŀ¼�����Ƶأ�os.path.exists()�����������������·���Ƿ���ش��ڡ�
"""