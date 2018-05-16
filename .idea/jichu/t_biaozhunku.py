#python标准库
"""
sys模块
os模块
"""


#sys
"""
sys.version字符串给你提供安装的Python的版本信息。sys.version_info元组则提供一个更简单的
方法来使你的程序具备Python版本要求功能。
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
使用os.sep可以取代操作系统特定的路径分割符。
os模块：
● os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
● os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
● os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
● os.listdir()返回指定目录下的所有文件和目录名。
● os.remove()函数用来删除一个文件。
● os.system()函数用来运行shell命令。
● os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
● os.path.split()函数返回一个路径的目录名和文件名。
>>> os.path.split('/home/swaroop/byte/code/poem.txt')
('/home/swaroop/byte/code', 'poem.txt')
● os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。类似地，os.path.exists()函数用来检验给出的路径是否真地存在。
"""