import time
import unittest
import HTMLTestRunner
from appium import webdriver

class SecurityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desire_caps  = dict()
        desire_caps ["platformName"] = "Android"
        desire_caps ["deviceName"] = "HC49AMY01284"
        desire_caps ["platfromVersion"] = "6.0"
        desire_caps ["appActivity"] = ".ui.main.HomeActivity"
        desire_caps ["appPackage"] = "com.qihoo.security"
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)

    time.sleep(15)

    def test_Boost(self):
        self.driver.find_element_by_xpath("//*[@text='Boost']").click()
        time.sleep(15)
        assertt = self.driver.find_element_by_id("com.qihoo.security:id/result_title_text").text
        self.assertEqual(assertt,"OPTIMAL",msg="BOOST FAIL")
        time.sleep(10)
        self.driver.find_element_by_id("com.qihoo.security:id/home_meun").click()

    time.sleep(15)

    def test_Clean(self):
        self.driver.find_element_by_xpath("//*[@text='Clean']").click()
        time.sleep(10)
        self.driver.find_element_by_id("com.qihoo.security:id/custom_button_text").click()
        time.sleep(10)
        assertt = self.driver.find_element_by_id("com.qihoo.security:id/result_description_text").text
        self.assertEqual(assertt,"Cleaned",msg="CLEAN FAIL")
        time.sleep(10)
        self.driver.find_element_by_id("com.qihoo.security:id/home_meun").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(SecurityTest('test_Boost'))
    suite.addTest(SecurityTest('test_Clean'))
    report_time = time.strftime('%Y%m%d %X', time.localtime())
    report_name = '/Users/shiyonglin/Desktop/script/report/' + report_time + '-report.html'
    fp = open(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='360SecurityReport',
        description='Case Execution'
    )
    runner.run(suite)
    fp.close()


