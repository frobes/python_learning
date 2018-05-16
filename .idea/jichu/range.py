# -*- coding:utf-8 -*-
import sys

import time


for i in range(5):
  print i,
  #sys.stdout.flush()
  time.sleep(3)
  

#等价
sys.stdout.write('hello' + '\n')
print 'hello'