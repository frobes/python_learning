"""
控制流
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
    #如果用了r来代替\转义，则print时都用""
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
    guess == int(raw_input("请输入一个整数："))
    这里用==的话会导致guess是前面的值，结果guess一直小于number,应该用=赋值
    """
    guess = int(raw_input("请输入一个整数："))
    
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
#等价于for i in [1,2,3,4]
for i in range(1,5):
    print i
    i = i+1
    #停顿两秒
    time.sleep(2)
else:
    print r"The for loop is over!"
    
    
    
#break
"""
break从for或while循环终止，任何对应的循环else块也不会执行。
"""

# -*- coding:utf-8 -*-

while True:
  s = raw_input("请输入任意字符数字:")
    
  if s == "quit":
    break
  print r"THE LENGTH of the s is :",len(s)
print r"DONE!"



#continue
"""
跳过当前循环块的剩下语句，继续下一轮循环！
"""

while True:
    s = raw_input("ENTER something:")
    
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print r"THE LENGTH of the s is:",len(s)
print r"DONE!"





    

