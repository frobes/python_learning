"""
����a2 + b2 + c2 + ....
"""
#�ɱ�������Ǵ���Ĳ��������ǿɱ�ģ�������1����2�������������������0������*numbers
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum + n * n
    return sum

#������ǿɱ����������������ȷ�������õ�ʱ����Ҫ����װ��һ��list��tuple
#calc([1,2,3])
#calc((1,3,5,7))
#���ÿɱ���������ú����ķ�ʽ���Լ򻯳�����
print(calc(1,2,3))
print(calc(1,3,5,7))


def person(name, age, *, city, job):
    print(name, age, city, job)
    
person('Jack', 24, city='Beijing', job='Engineer')