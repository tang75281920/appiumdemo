from time import sleep

from appium import webdriver

"""
针对星球庄团测试
1、复习webview相关知识点


demo下载：https://xqdownload.2345.com/xq_apk/xingqiugw.apk
"""


class TestDemo:
    def setup(self):
        caps = {
            'platformName': 'Android',
            'appPackage': 'com.planet.light2345',
            'appActivity': '.launch.LaunchActivity',
            'noReset': True,
            'skipServerInstallation': True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_demo_webview(self):
        print(self.driver.context)  # 打印当前context
        print(self.driver.contexts)  # 打印所有的context
        self.driver.find_element_by_xpath('//*[@text="社会我王哥"]').click()

        #webview = self.driver.contexts[-1]
        #self.driver.switch_to.context(webview)  # 切换到webview
        print(self.driver.context)  # 打印当前context

        # 通父控件定位子控件，点击首页的果园
        self.driver.find_element_by_xpath('//*[@resource-id="com.planet.light2345:id/llFunc"]/android.widget.ImageView[1]').click()




        self.driver.switch_to.context(self.driver.contexts[0])  # 切回native
        print(self.driver.context)  # 打印当前context

    def teardown(self):
        sleep(4)
        self.driver.quit()
