from selenium.webdriver.common.by import By
from appiumframework.PO.base_page import BasePage

class BoostPage(BasePage):

    #def __init__(self, driver):
        #self.driver = driver

    #u '加速页'
    return_button = (By.ID, "com.qihoo.security:id/home_meun")
    finish_text = (By.ID, "com.qihoo.security:id/result_title_text")
    def click_return_button(self):
        return self.find_element(*self.return_button).click()
    def finish_text_name(self):
        return self.find_element(*self.finish_text).text