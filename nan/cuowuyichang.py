#coding=utf-8
'''
python中的异常：
1、NameError:尝试访问一个未申明的变量
2、ZeroDivisionError:除数为零
3、SyntaxError:python解释器语法错误
4、IndexError:请求的索引超出序列范围
5、KeyError:请求一个不存在的字典关键字
6、IOError:输入/输出错误
7、AttributeError:尝试访问未知的对象属性

'''


'''
try:
    try_suite   #监控这里的异常
except Exception1:
    suite_for_Exception1   #异常处理代码
except (Exception2,Exception3,Exception4):
    suite_for_Exception2_3_4
except Exception5,Argument5:
    suite_for_Exception5_plus_argument
except (Exception6,Exception7),Argument67:
    suite_for_Exception6_7_plus_argument
except:
    suite_for_all_other_exceptions
else:
    no_exceptions_detected_suite
finally:
    always_execute_suite

'''