import  json
def greet_user():
    '''问候用户，并指出其名字'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("what's your name?")
        with open(username,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back,"+username+"!")
    else:
        print("Welcome back,"+username+"!")

greet_user()

#重构
#将获取存储的用户名的代码转移到另一个函数中
import  json
def get_stored_username():
    '''如果存储了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return username

def greet_user():
     '''问候用户，并指出其名字'''
     username = get_stored_username()
     if username:
         print("Welcome back,"+username+" !")
     else:
        username = input("what's your name?")
        with open(username,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back,"+username+"!")

greet_user()


#重构
#将greet_user()的另一个代码块提取出来：将没有存储用户名时提示用户输入的代码放在一个独立的函数中
import  json
def get_stored_username():
    '''如果存储了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return username

def get_new_username():
    '''提示用户输入用户名'''
    username = input("what's your name?")
    filename = 'username.json'
    with open(username,'w') as f_obj:
        json.dump(username,f_obj)
    return  username

def greet_user():
     '''问候用户，并指出其名字'''
     username = get_stored_username()
     if username:
         print("Welcome back,"+username+" !")
     else:
         username = get_new_username()
         print("We'll remember you when you come back,"+username+"!")
greet_user()

