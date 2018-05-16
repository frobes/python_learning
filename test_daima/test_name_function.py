#模块unittest提供了代码测试工具。
#单元测试用于核实函数的某个方面没有问题，测试用例是一组单元测试。
#为函数编写测试用例，可先导入模块unittest以及要测试的函数，在创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
'''
import  unittest
from name_function import  get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理像janis joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        #断言：核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Janis Joplin')

#让python运行这个文件中的测试
#unittest.main()
print("\n---------------------2-----------------------")

import  unittest
from name_function import  get_formatted_name2
class NamesTestCase2(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理像janis joplin这样的姓名吗？"""
        formatted_name = get_formatted_name2('janis','joplin')
        #断言：核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Janis Joplin')
#unittest.main()
print("\n---------------------3-----------------------")

import  unittest
from name_function import  get_formatted_name3

class NamesTestCase3(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理像janis joplin这样的姓名吗？"""
        formatted_name = get_formatted_name3('janis','joplin')
        #断言：核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()
print("\n---------------------4-----------------------")
'''

import  unittest
from name_function import  get_formatted_name3

class NamesTestCase3(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理像janis joplin这样的姓名吗？"""
        formatted_name = get_formatted_name3('janis','joplin')
        #断言：核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像janis joplin aplh这样的姓名吗？"""
        formatted_name = get_formatted_name3('janis','joplin','aplh')
        #断言：核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,'Janis Aplh Joplin')

unittest.main()