from time import sleep

from appium import webdriver

"""
09：
PO模式修改前的测试脚本
修改后的键python package：page和testcase

测试apk
- 雪球

blog:
- https://blog.csdn.net/tt75281920/article/details/116429894
"""


class TestDemo:
    def setup(self):
        caps = {
            'platformName': 'Android',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            'skipServerInstallation': True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        """
        原脚本
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()  # 点击首页搜索框
        self.driver.find_element_by_id("search_input_text").send_keys('二三四五')  # 输入股票代码
        self.driver.find_element_by_id("name").click()  # 点输入联想列表的股票名称

        price = self.driver.find_element_by_id("current_price")  # 获取股票价格

        assert float(price.text) > 1.0  # 断言是否大于1元

    def teardown(self):
        sleep(4)
        self.driver.quit()


