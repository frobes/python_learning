def mod(x):
    return x*x

while True:
    i = int(raw_input("请输入随机一个数："))
    
    print("该数的平方是%d"%mod(i))
    
    if i==3:
        break