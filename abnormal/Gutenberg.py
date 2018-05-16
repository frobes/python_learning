#分析文本
#提取通话Alice in Wonderland的文本，计算它包含多少单词。
filename='alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词。
    words = contents.split()
    num_words = len(words)
    print("The file "+filename+ "has about "+ str(num_words) + " words.")
print("\n----------------------------------------------")

#使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file "+filename+" does not exist."
        print(msg)
    else:
        #计算文件大致包含多少个单词。
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+ "has about "+ str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)
print("\n----------------------------------------------")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt']
for file in filenames:
    count_words(file)
print("\n----------------------------------------------")

#文件找不到时一声不吭pass
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件大致包含多少个单词。
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+ "has about "+ str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt']
for file in filenames:
    count_words(file)




