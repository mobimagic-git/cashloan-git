from appium import webdriver
import time
import unittest
from appiumframework.PO.base_page import BasePage
from appiumframework.Pages.home_page import HomePage
from appiumframework.Pages.boost_page import BoostPage
from appiumframework.Pages.clean_page import CleanPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appiumframework.Pages import home_page
from appiumframework.Pages import boost_page
from appiumframework.Pages import clean_page

class SecurityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desire_caps  = dict()
        desire_caps ["platformName"] = "Android"
        desire_caps ["deviceName"] = "ZX1C323524"
        desire_caps ["platfromVersion"] = "5.1.1"
        desire_caps ["appActivity"] = ".ui.main.HomeActivity"
        desire_caps ["appPackage"] = "com.qihoo.security"
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)

    time.sleep(15)

        #cls.home_page = HomePage(cls.driver)
        #cls.boost_page = BoostPage(cls.driver)
        #cls.clean_page = CleanPage(cls.driver)

    #def setUp(self):
        #self.home_page = HomePage(self.driver)

    #def setUp(self):
        #self.boost_page = HomePage(self.driver)

    #def setUp(self):
        #self.clean_page = HomePage(self.driver))


    def test_Boost(self):

        HomePage(self.driver).click_boost_button()
        time.sleep(15)
        assertt = BoostPage(self.driver).finish_text_name()
        self.assertEqual(assertt,"已达最佳",msg="加速失败！")
        time.sleep(10)
        BoostPage(self.driver).click_return_button()
        time.sleep(15)


    def test_Clean(self):

        HomePage(self.driver).click_clean_button()
        time.sleep(10)
        HomePage(self.driver).click_cleannow_button()
        assertt = CleanPage(self.driver).finish_text_name()
        self.assertEqual(assertt,"已清理",msg = "清理失败！")
        time.sleep(10)
        CleanPage(self.driver).click_return_button()
        time.sleep(10)



    @classmethod
    def tearDownClass(cls): # 不要忘记收尾。
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()