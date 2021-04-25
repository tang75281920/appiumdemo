from time import sleep

from appium import webdriver

"""
08：
对于webview的测试

测试apk：雪球demo下载：

blog:
- 
"""


class TestDemo:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = True
        caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_demo_webview(self):
        print(self.driver.contexts)
        self.driver.find_element_by_xpath('//*[@text="交易"]').click()

        for i in range(5): print(self.driver.contexts)

        #self.driver.find_element_by_xpath('//*[@text="去开户"]').click()
        self.driver.find_element_by_xpath('//*[@text="免费领"]').click()

        # todo 不用切换webview也能正常操作webview的元素
        # 切换到 webview
        #webview = self.driver.contexts[-1]
        #self.driver.switch_to.context(webview)
        #print(self.driver.context)


        # self.driver.find_element_by_id('phone-number').send_keys('18600000886') # 直接使用resource-id定位找不到元素，使用xpath就可以
        self.driver.find_element_by_xpath("//*[@resource-id='phone-number']").send_keys('18600000886')
        self.driver.find_element_by_xpath('//*[@text="获取验证码"]').click()
        # 返回到原生view
        #self.driver.switch_to.context(self.driver.contexts[0])
        #print(self.driver.context)

    def teardown(self):
        sleep(4)
        self.driver.quit()
