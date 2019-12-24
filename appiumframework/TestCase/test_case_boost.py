from appium import webdriver
import time
import unittest
from appiumframework.Pages.home_page import HomePage
from appiumframework.Pages.boost_page import BoostPage
from appiumframework.Pages.clean_page import CleanPage


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

        HomePage(self.driver).click_boost_button()
        time.sleep(15)
        assertt = BoostPage(self.driver).finish_text_name()
        self.assertEqual(assertt,"OPTIMAL",msg="BOOST FAIL")
        time.sleep(10)
        BoostPage(self.driver).click_return_button()
        time.sleep(15)


    def test_Clean(self):

        HomePage(self.driver).click_clean_button()
        time.sleep(10)
        HomePage(self.driver).click_cleannow_button()
        assertt = CleanPage(self.driver).finish_text_name()
        self.assertEqual(assertt,"Cleaned",msg = "CLEAN FAIL")
        time.sleep(10)
        CleanPage(self.driver).click_return_button()
        time.sleep(10)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
