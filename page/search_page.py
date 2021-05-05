from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)  # 输入股票代码
        self.driver.find_element_by_id("name").click()  # 点输入联想列表的股票名称
        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)
