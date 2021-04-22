from time import sleep

from appium import webdriver

"""
05：
appium调用uiautomator完成元素定位，操作

官方文档：
- http://appium.io/docs/en/writing-running-appium/finding-elements/
- http://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html

demo下载：
- https://github.com/appium/java-client/blob/master/src/test/resources/apps/ApiDemos-debug.apk
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

    def test_demo_1(self):
        # 通过className定位
        # 定位到第二个textview
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").instance(1)').click()

    def test_demo_2(self):
        # 通过text定位
        # 定位到第一个文本属性为‘Animation’的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")').click()

    def test_demo_3(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")').click()
        # 使用（找到的第一个）滚动元素，一直滑动至（通过文本定位的）'Tabs'元素出现
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Tabs")').click()
        sleep(19)

    def test_demo_4(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")').click()
        # 通过找到的第一个滚动元素，滚动定位到第一个文本为'Popup Menu'元素
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()
        sleep(19)

    def teardown(self):
        sleep(5)
        self.driver.quit()
