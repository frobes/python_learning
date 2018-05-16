#print absolute value of  an integer:

a = int(raw_input('请输入任意一个数：'))
#a = input('请输入任意一个数：')
if a >= 0 :
    print(a)
else:
    print(-a)
    
    
    
age = raw_input("请输入你的年龄：\n")
if int(age) >= 18:
    print("you are an adult!your age is:"+age)
else:
    print("you are teenager\n")