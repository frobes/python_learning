"""
������
if
while
for
break
continue
"""

# -coding:utf-8 -*-
#if
number = 23
guess = int(raw_input("please enter a integer..."))

if guess == number:
    print 'congratulation you guessed it!'
    print r"but you don't in any prizes"
elif guess < number:
    print r"It's is higher than that!"
else:
    #�������r������\ת�壬��printʱ����""
    print r"NO,it's a little lower than that!'"
    
print 'Done!'



if True:
    print 'YES,this\'s true!'




#while
# -*- coding:utf-8 -*-
number = 23
running = True

while running:
    """
    guess == int(raw_input("������һ��������"))
    ������==�Ļ��ᵼ��guess��ǰ���ֵ�����guessһֱС��number,Ӧ����=��ֵ
    """
    guess = int(raw_input("������һ��������"))
    
    if guess == number:
        print r"congratulation,you're guess it!"
        running = False
    elif guess > number:
        print r"no, it's a little higher than that!"
    else:
        print r"no,it's a little lower than that!"     
else:
    print r"the while loop is over!"
    
print r"DONE!IT'S SUSSESSFULL."



#for
# -*- coding:utf-8 -*-
import time
#�ȼ���for i in [1,2,3,4]
for i in range(1,5):
    print i
    i = i+1
    #ͣ������
    time.sleep(2)
else:
    print r"The for loop is over!"
    
    
    
#break
"""
break��for��whileѭ����ֹ���κζ�Ӧ��ѭ��else��Ҳ����ִ�С�
"""

# -*- coding:utf-8 -*-

while True:
  s = raw_input("�����������ַ�����:")
    
  if s == "quit":
    break
  print r"THE LENGTH of the s is :",len(s)
print r"DONE!"



#continue
"""
������ǰѭ�����ʣ����䣬������һ��ѭ����
"""

while True:
    s = raw_input("ENTER something:")
    
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print r"THE LENGTH of the s is:",len(s)
print r"DONE!"





    

