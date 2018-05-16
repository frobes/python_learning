
'''ʵ��
*
* *
* * *
* * * *
* * * * *
#coding=utf-8


#��������
i = 1

while i<=5:
    #����1    
    #print("*"*i)
    
    #������
    #����һ���еĸ���
    j = 1
    while j<=i:
        #python2д��
        print "x",'',
        #python3д�� ��print("* ",end='')
        
        j+=1
    #�ڶ���while����Ҫ���У������while��Ҫ����
    print("")
    i+=1
'''


    
'''ʵ��
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


#��������
i = 1

while i<=5:
    #����1    
    #print("*"*i)
    
    #������
    #����һ���еĸ���
    j = 1
    while j<=i:
        #python2д��
        print "x",'',
        #python3д�� ��print("* ",end='')
        
        j+=1
    #�ڶ���while����Ҫ���У������while��Ҫ����
    print("")
    i+=1

while i>=2:
    #����1    
    #print("*"*i)
    
    #������
    #����һ���еĸ���
    j = 1
    while j<(i-1):
        #python2д��
        print "x",'',
        #python3д�� ��print("* ",end='')
        
        j+=1
    #�ڶ���while����Ҫ���У������while��Ҫ����
    print("")
    i-=1
'''



'''
9*9�˷���
'''
#����һ��ѭ����������
i = 1


while i<=9:
    
    #����һ��ѭ������ÿ�е�����
    j = 1
    while j<=i:
        print  "%d*%d=%2d "%(j,i,i*j),'',
        j+=1
    
    print("")
    i+=1
