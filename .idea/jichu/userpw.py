#coding=utf-8

"""
模拟用户登录
"""

#做为用户数据库
db = {}

#建立新用户
def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            promt = 'name taken,try another:'
            continue
        else:
            break
        
    pwd = raw_input('passwd:')
    db[name] = pwd
    
    
#处理返回的用户
def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    
    if passwd == pwd:
        print 'welcome back',name
    else:
        print 'login incorrect!'

#真正控制脚本的是showmenu()函数 
def showmenu():
    prompt = """
    -------------------------
    (N)ew user login
    (E)xisting user login
    (Q)uit
    Enter choice: """

    #done = False
    while True:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice = 'q' 
            print '\nYou picked:[%s]'%choice
           
            if choice not in 'neq':
                print 'invalid option,try again!'
            else:
                chosen = True
       
                    
            if choice == 'q':done = True
            if choice == 'n':newuser()
            if choice == 'e':olduser()
                     
        
if __name__=='__main__':
    showmenu()
    
    
        
        

