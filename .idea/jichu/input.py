# -*- coding:utf-8 -*-
import sys
#2.7版本中input返回的是数值类型，raw_input()返回的是字符串--string类型
name = 66
name = input('please input a number:')
string=raw_input('please input a string:')
print('hello', name, string)

#TypeError: function takes exactly 1 argument (2 given)
#sys.stdout.write('hello',string)
#TypeError: expected a string or other character buffer object
#sys.stdout.write(name)

sys.stdout.write('hello')
sys.stdout.write(string)