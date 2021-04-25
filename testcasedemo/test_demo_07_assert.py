from appium import webdriver
from hamcrest import *

"""
07：
断言：
- pytest assert
- hamcrest

demo下载：
- https://github.com/appium/java-client/blob/master/src/test/resources/apps/ApiDemos-debug.apk

blog:
- 
"""


class TestDemo:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = '.ApiDemos'
        caps['noReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_demo_pytest_assert(self):
        # 点击Views
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")').click()
        # 点击Popup Menu
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()

        self.driver.find_element_by_accessibility_id('Make a Popup!').click()
        assert len(self.driver.find_elements_by_xpath('//*[@text="Edit"]')) == 1  # 断言是否存在'Edit'文案

        self.driver.find_element_by_xpath('//*[@text="Search"]').click()

        toast = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]')
        assert 'Clicked popup menu item Search' in toast.text  # 断言toast文案是否为'Clicked popup menu item Search'

        assert len(toast.text) > 10  # 断言toast文案长度大于10
        assert 'Clicked popup menu item Search' in toast.get_attribute(
            'text')  # 断言toast的text属性为'Clicked popup menu item Search'

        assert_that(toast.get_attribute('text'), equal_to('Clicked popup menu item Search'))  # hamcrest形式的断言

    def teardown(self):
        self.driver.quit()
