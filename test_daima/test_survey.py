#导入模块unittest以及要测试的类AnonymousSurvey
import unittest
from survey import AnonymousSurvey

#继承类unittest.TestCase
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        #检查English是否包含在列表my_survey.responses中
        self.assertIn('English',my_survey.responses)

unittest.main()
