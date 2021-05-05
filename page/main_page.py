from selenium.webdriver.remote.webdriver import WebDriver

from page.search_page import SearchPage


class MainPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()  # 点击首页搜索框
        return SearchPage(self.driver)
