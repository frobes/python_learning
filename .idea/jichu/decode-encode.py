'''
an example of reading
д���ļ������ݿ������ʱ����encode()����
��ȡ������decode()����
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

