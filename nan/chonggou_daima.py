#/usr/bin/evn/python
# coding=utf-8
'''
寻找文件最长的行
'''
#读取文件
f = open('E:\workspace\test\nan\schonggou_daima.py','r')
longest = 0
while True:
    linelen = len(f.readline().strip())
    if not linelen:break
    if linelen > longest:
        longest = linelen
f.close()
return longest


'''
尽早释放文件资源
'''
f = open('E:\workspace\test\nan\schonggou_daima.py','r')
longest = 0
alllines = f.readlines()
f.close()
for line in alllines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
return longest

'''
列表解析简化代码
调用字符串strip()方法处理行内容
'''
f = open('E:\workspace\test\nan\schonggou_daima.py','r')
longest = 0
alllines = [x.strip() for x in f.readlines()]
f.close()
for line in alllines:
    linelen = len(line)
    if linelen > longest:
        longest = linelen
return longest


'''
以上两个例子在处理大文件有问题，因为readline会读取文件的所有行，后来有了迭代器，文件本身就成为了它的迭代器，不需要调用readlines()函数。
既然已经做到这一步，为什么不直接获得行长度的集合（之前得到的是行的集合）
使用max()函数得到最长的字符串的长度
'''
f = open('E:\workspace\test\nan\schonggou_daima.py','r')
alllines = [len(x.strip()) for x in f]
f.close()
return max(alllines)

'''
以上例子问题：一行一行迭代f的时候，列表解析需要把文件所有行读取到内存中，然后生成列表。
简化代码：使用生成器表达式替换列表解析，把它移到max()函数里，这样，所有的核心只有一行。
'''
f = open('E:\workspace\test\nan\schonggou_daima.py','r')
longest = max(len(x.strip()) for x in f)
f.close()
return longest

'''
去掉文件打开模式（默认为读取），然后用python去处理打开的文件
ps:生成器表达式在python2.4中被加入。
'''
return max(len(x.strip()) for x in open('E:\workspace\test\nan\schonggou_daima.py'))


















