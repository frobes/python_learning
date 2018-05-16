#使用模块json存储数据
#json能让简单的python数据结构转储到文件中，并在程序再次运行时加载文件中的数据。

#json.dump()和json.load()

#number_writer.py
import  json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
#使用函数json.dump()将数字列表存储到文件numbers.json
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
    #AttributeError: module 'json' has no attribute 'dump'


#number_reader.py
import  json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)


#remember_me.py
import  json
username = input("what's your name?")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, "+username+" !")

#greet_user.py
import  json
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back,"+username+" !")


#try代码块
import  json
#如果以前存储了用户名就加载，否则提示用户输入用户名并存储它。
filename = 'username.json'
try:
    with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError:
    username = input("what's your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+" !")
else:
     print("Welcome back,"+username+" !")