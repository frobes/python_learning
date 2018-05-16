#导入模块unittest以及要测试的类AnonymousSurvey
import unittest
from survey import AnonymousSurvey

#继承类unittest.TestCase
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    #如果在TestCase类中包含了方法setUp(),python将先运行它，再运行各个以test_开头的方法。
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)

        #循环来确认每个答案是否包含在列表my_survey.responses中
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
