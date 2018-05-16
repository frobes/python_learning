# -*- coding: utf-8 -*-
# @Time : 2017/10/1 16:22 
# @File : Difflib.py 
# @Software: PyCharm

import difflib

text1 = """ 
This is Text1
人生苦短，我用Python！
Python！Python！Python！
"""

text2 = """ 
This is Text2
人生苦短，我用Python！
Python!Python!Python!
"""
text1_lines = text1.splitlines()    # 分别以行进行分割
text2_lines = text2.splitlines()

d = difflib.Differ()                # 创建Differ对象
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(list(diff)))