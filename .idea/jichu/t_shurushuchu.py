#�������
'''
�ļ�
������
'''


#�ļ�

"""
����һ��file����������ļ�����д�ļ���file���read��readline��write���������ļ��Ķ�д�����������ڴ��ļ�ʱָ����ģʽ��
�ر��ļ���close������

"""


#filename:using_file.py


poem='''\
Pragraming is fun when the work is done.
if you wanna make you work also fun:
 use Python!
'''

#����һ��file���ʵ����ģʽ����Ϊ��ģʽ��'r'����дģʽ��'w'����׷��ģʽ��'a'�����ǵü�ð��''
f=file('poem.txt','w') #open for writing

f.write(poem) #д��poem��poem.txt

f.close()

f=file('poem.txt')

while True:
    line=f.readline()
    if len(line) == 0:
        break
    print line,
    
f.close()

#End of using_file.py



#������pickle
"""
Python�ṩһ����׼��ģ�飬��Ϊpickle��ʹ����������һ���ļ��д����κ�Python����֮
���ֿ��԰���������ȱ��ȡ�������ⱻ��Ϊ �־õش������
��һ��ģ���ΪcPickle�����Ĺ��ܺ�pickleģ����ȫ��ͬ��ֻ����������C���Ա�д�ģ����Ҫ��öࣨ��pickle��1000������
"""
#filename:picking.py
#import..as�﷨
import pickle as p


shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']

f=file(shoplistfile,'w')
#���ô�����ģ���dump�������Ѷ��󴢴浽�򿪵��ļ��С�������̳�Ϊ���� ��
p.dump(shoplist,f)
f.close()

f=file(shoplistfile)
#ʹ��pickleģ���load�����ķ�����ȡ�ض���������̳�Ϊȡ���� ��
storelist=p.load(f)
print storelist