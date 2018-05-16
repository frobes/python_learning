'''from imptee import  foo,show
show()
foo = 123
print("foo from impter:",foo)
show()
'''

#使用import和完整的标识符名称

import  imptee
imptee.show()
imptee.foo = 123
print("foo from impter:",imptee.foo)
imptee.show()

'''输出：
foo  from imptee: abc
foo from impter: 123
foo  from imptee: 123
'''
