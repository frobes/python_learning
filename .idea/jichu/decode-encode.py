'''
an example of reading
写入文件或数据库或网络时调用encode()函数
读取数据用decode()函数
'''

CODEC = 'utf-8'
file = 'unicode.txt'

hello_out = u"HELLO WORLD \n"
bytes_out = hello_out.encode(CODEC)

f = open(file,"w")
f.write(bytes_out)
f.close()

f = open(file,"r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)

print hello_in

