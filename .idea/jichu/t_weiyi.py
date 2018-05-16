import math

def move(x,y,step,angle=0):
    nx=x + step * math.cos(angle)
    ny=y - step * math.sin(angle)
    return nx, ny

x,y=move(100,100,60,math.pi/6)

print (x,y)



"""
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。
"""
# -*- coding:utf-8 -*-
import math

def quaratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number!')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number!')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number!')
    d = b * b - 4 * a * c
    
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根为全体实数。'
            else:
                return '方程无根'
            
        else:
            x1 = -c/b
            x2 = x1
            return x1,x2
    else:
        if d < 0:
            return '方程无根'
        else:
            x1 = ( -b + math.sqrt(d) ) / (2 * a )
            x2 = ( -b - math.sqrt(d) ) / (2 * a )
            return x1,x2
            

print(quaratic(2,3,1))
print(quaratic(1,3,-4))






