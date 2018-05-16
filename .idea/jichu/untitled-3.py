"""
计算a2 + b2 + c2 + ....
"""
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。如*numbers
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum + n * n
    return sum

#如果不是可变参数，参数个数不确定，调用的时候，需要先组装出一个list或tuple
#calc([1,2,3])
#calc((1,3,5,7))
#利用可变参数，调用函数的方式可以简化成这样
print(calc(1,2,3))
print(calc(1,3,5,7))


def person(name, age, *, city, job):
    print(name, age, city, job)
    
person('Jack', 24, city='Beijing', job='Engineer')