from appium import webdriver


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "d0a49989"
        caps["appPackage"] = "com.android.contacts"
        caps["appActivity"] = "com.android.contacts.activities.TwelveKeyDialer"
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        el1 = self.driver.find_element_by_accessibility_id("一")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("零")
        el2.click()
        el2.click()
        el3 = self.driver.find_element_by_accessibility_id("八")
        el3.click()
        el4 = self.driver.find_element_by_accessibility_id("六")
        el4.click()
        el5 = self.driver.find_element_by_accessibility_id("拨打电话")
        el5.click()

    def teardown(self):
        self.driver.quit()
