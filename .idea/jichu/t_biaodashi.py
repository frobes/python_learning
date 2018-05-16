"""
运算符与表达式
**  幂
//  整除
%   取模
<<  左移
>>  右移
&   按位与
|   按位或
^   按位异或
~   按位翻转
"""

# -*- coding:utf-8 -*-

length = int(raw_input("请输入长："))
brendth = int(raw_input("请输入宽："))
area = length * brendth
print  '长宽的面积是：',area
print '周长是：', 2*(length + brendth)

#字符和数字不能直接相加
area = str(area)
print  ('长宽的面积是：'+area)
print  ('长宽的面积是：',area)





