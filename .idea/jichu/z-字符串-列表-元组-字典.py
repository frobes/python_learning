'''


name = "abcdef"

print(name)

for  x in name:
    print(x)
    

i = 0
while i<6:
    print(name[i])
    i+=1
    

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#coding=utf-8
#1.����һ���б�������һЩ����
namesList = ["xiaohong","xiaoming","xiaozhang"]

while True:
    #2.��ȡһ��Ҫ���ҵ�����
    insertName = raw_input("������������֣�")
    if insertName=="quit":
        break
        
    #3.�ж��Ƿ���ڣ�����ʾ��Ӧ����ʾ
    findFlag = 0
    for name in namesList:
        if name==insertName:
            findFlag = 1
          
    
    if findFlag == 1:
        print("�ҵ���")
    else:
        print("û���ҵ�")
    


    #�ڶ��ַ���
    if insertName in namesList:
        print("�ҵ���")
    else:
        print("û���ҵ�")
    
  '''



'''

#coding=utf-8

#1.��ӡ��ʾ
print("="*30)

print("----��ӭʹ�û��������ϵͳ----")
print("1.���������")
print("2.ɾ��һ������")
print("3.�޸�һ������")
print("4.��ѯһ������")
print("5.������������")
print("0.�˳�ϵͳ")


#����һ���б�洢�������֣�
names = []

while True:   
    print("="*30)
    
    #2.��ȡҪ����������
    key = int(raw_input("��������Ҫ�����֣�"))
    
    
    #3.����ѡ��������Ӧ������   
    if key==1:
        #3.1��ʾ�û�����һ��������
        insertName = raw_input("������Ҫ��ӵ����֣�")
        #3.2��������ӵ��б���
        names.append(insertName)
    elif key==2:
        insertName = raw_input("������Ҫɾ�������֣�")
        names.remove(insertName)
    elif key==3:
        xxx
    elif key==4:
        insertName = raw_input("������Ҫ��ѯ�����֣�")
        d = names.index(insertName)
        print("�������±��ǣ�%d"%d)
    elif key==5:
        for name in names:
            print "ϵͳ�����У�%s"%name,'', 
        print ''            
    elif key==0:
        break
    else:
        print("����������������֣�0-5")

print("="*30)
print("���Ѿ��˳�ϵͳ��")

'''
  
  
#coding:utf-8
import random

#1.����һ���б�Ƕ�׵��б�
rooms = [[],[],[]]

#2.����һ���б�����8����ʦ�����֣��洢����������б�
teachers = ["A","B","C","D","E","F","G","H"]

#3.�����8����ʦ��������ӵ���1���б���
for name in teachers:
  randnum = random.randint(0,2)  
  
  rooms[randnum].append(name)
  
#print(rooms)

#4.��� ��ʾ
i = 1
for room in rooms:
  #print(room)
  
  print("�칫��%d�������ʦ�����ǣ�"%i)
  for name in room:
    print  name,'',
  print ''
  i+=1
