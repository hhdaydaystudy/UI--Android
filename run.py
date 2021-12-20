# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import unittest
import HTMLTestRunner
from case1 import MyTestCase1
from case2 import MyTestCase2

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCase1))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCase2))

    # 这一步是在当前文件夹里自动生成一个测试报告，测试报告名称就叫：UnittestTextReport.txt.
    with open('HTMLReport.html', 'wb') as f:
         runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                title='逐梦教育-UI-自动化',
                                description='测试报告.',
                                verbosity=2)

         runner.run(suite)
