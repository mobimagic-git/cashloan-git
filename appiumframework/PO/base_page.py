from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage(object):
    #初始化
    def __init__(self, driver):
        self.driver = driver

    #重写定位元素
    def find_element(self, *loc):  # *loc任意数量的位置参数（带单个星号参数）
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('页面未找到%s元素' % (loc))

