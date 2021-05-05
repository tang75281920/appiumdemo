from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        (By.ID, "image_cancel"),
        (By.ID, "tips")
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)  # todo 最好是使用递归的方式（还需要考虑遇到没出现的弹框导致的死循环）

    def find_element_and_click(self, locator):
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):  # 找元素找不到的一个处理逻辑
        self.driver.implicitly_wait(0)  # 提升处理的效率
        """方法一"""
        for locator in self._black_list:
            elements = self.driver.find_elemenst(*locator)
            if len(elements) >= 1:
                elements[0].click()
            else:
                print("%s not found" % str(locator))

        """方法二：使用page source会更快的定位"""
        # page_source=self.driver.page_source
        # if "image_cancel" in page_source:
        #     self.driver.find_element(*locator).click()
        # elif "tips" in page_source:
        #     pass
        self.driver.implicitly_wait(10)
