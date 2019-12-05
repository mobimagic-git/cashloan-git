import time
import os
import unittest
import HTMLTestRunner
from appium import webdriver


cur_path = os.getcwd()
testcase_path = os.path.join(cur_path,"TestCase")
report_path = os.path.join(cur_path,"Report")


#def creat_suite():
    #suite = unittest.TestSuite()
    #discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    #for test_suite in discover:
        #print(test_suite)
        #for test_case in test_suite:
             #suite.addTest(test_case)
    #return suite
  #suite = creat_suite()

if __name__ == '__main__':
    testlist = unittest.defaultTestLoader.discover(testcase_path, pattern='test*.py')
    report_time = time.strftime('%Y%m%d %X', time.localtime())
    report_title = '360Security测试报告' + report_time + '.html'
    result_path = os.path.join(report_path,report_title)

    fp = open(result_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=report_title,
        description='用例执行情况'

    )
    runner.run(testlist)
    fp.close()


