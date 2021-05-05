from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.main_page import MainPage


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        """
        启动app：后进入首页
        :return: 首页
        """
        caps = {
            'platformName': 'Android',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            'skipServerInstallation': True
        }

        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls.driver.implicitly_wait(10)

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
