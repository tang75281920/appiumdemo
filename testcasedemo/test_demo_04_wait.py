from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
04：
编写脚本时，常用的3种等待方式
"""


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "d0a49989"
        caps["appPackage"] = "com.android.contacts"
        caps["appActivity"] = "com.android.contacts.activities.TwelveKeyDialer"
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

        self.driver.implicitly_wait(10)  # 隐式等待

    def test_demo_sleep(self):
        sleep(10)  # 强制等待
        if len(self.driver.find_elements_by_accessibility_id('一')) >= 1:
            self.driver.find_element_by_accessibility_id("一").click()

        el2 = self.driver.find_element_by_accessibility_id("零")
        el2.click()
        el2.click()
        el3 = self.driver.find_element_by_accessibility_id("八")
        el3.click()
        el4 = self.driver.find_element_by_accessibility_id("六")
        el4.click()
        el5 = self.driver.find_element_by_accessibility_id("拨打电话")
        el5.click()

    def test_demo_wait_1(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.ID, "一")))  # 隐式等待，但并非最优方案，可以用来等待固定的元素，不能用来确认临时元素，如升级弹窗之类
        self.driver.find_element_by_accessibility_id("一").click()
        self.driver.find_element_by_accessibility_id("零").click()
        self.driver.find_element_by_accessibility_id("八").click()
        self.driver.find_element_by_accessibility_id("八").click()
        self.driver.find_element_by_accessibility_id("六").click()

    def test_demo_wait_2(self):
        def loaded(driver):
            if len(self.driver.find_elements_by_accessibility_id('一')) >= 1:
                self.driver.find_element_by_accessibility_id("一").click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 15).until(loaded)  # 处理不确定元素的方式，如可能出现的升级弹窗之类，不过也只能针对已知页面的不确定性弹窗，对于不确定哪个页面的弹窗，之后会介绍watch机制
        except:
            print('no 1')

    def teardown(self):
        self.driver.quit()
