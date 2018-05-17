#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/26 下午2:41
# @Author : xiaowei
# @Site : 
# @File : testtime.py
# @Software: PyCharm
import time
import datetime

print(time.time())

localTime = time.localtime(time.time())
strTime = time.strftime("%Y-%m-%d", localTime)
#strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
print(strTime)