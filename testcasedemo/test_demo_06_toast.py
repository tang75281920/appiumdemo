from time import sleep

from appium import webdriver

"""
05：
appium识别toast

demo下载：
- https://github.com/appium/java-client/blob/master/src/test/resources/apps/ApiDemos-debug.apk

blog:
- https://blog.csdn.net/tt75281920/article/details/116011065
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

    def test_demo_toast(self):
        # 点击Views
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")').click()
        # 点击Popup Menu
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()

        self.driver.find_element_by_accessibility_id('Make a Popup!').click()
        self.driver.find_element_by_xpath('//*[@text="Search"]').click()
        # 打印toast的内容
        print(self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text)

    def teardown(self):
        sleep(5)
        self.driver.quit()
