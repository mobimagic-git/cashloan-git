from selenium.webdriver.common.by import By
from appiumframework.PO.base_page import BasePage

class HomePage(BasePage):

    #def __init__(self, driver):
        #self.driver = driver

    #u '首页'
    boost_button = (By.XPATH,"//*[@text='Boost']")
    clean_button = (By.XPATH,"//*[@text='Clean']")
    cleannow_button = (By.ID,"com.qihoo.security:id/custom_button_text")
    def click_boost_button(self):
        return self.find_element(*self.boost_button).click()
    def click_clean_button(self):
        return self.find_element(*self.clean_button).click()
    def click_cleannow_button(self):
        return self.find_element(*self.cleannow_button).click()




