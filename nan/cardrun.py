import  os
def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError,TypeError),diag:
        retval = str(diag)
    return retval

def main():
    'handle all the data processing'
    log = open('cardlog.txt','w')
    #从文件中读取数据，文件打开置于try...except语句段中
    #同时还有一个处理日志文件。
    try:
        ccfile = open('cardlog.txt','r')
    except  IOError,e：
        log.write('no txns this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')
    #数据被读入txns列表，随便遍历txns
    for eachTxn in txns:
        #每次调用safe_float()后，用内建的isinstance函数检查结果类型
        result = safe_float(eachTxn)
        if isinstance(result,float):
            total += result
            log.write('data....processed\n')
        else:
            log.write('ignored:%s'%result)
    print('$%.2f(new balance)'%total)
    log.close()

if __name__='__main__':
    main()


'''
#cat carddata.txt
previous balance
25
debits
21.64
241.24
25
credits
-25
-541.4
finance charge/late fees
7.30
5
'''
