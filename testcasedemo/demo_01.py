from time import sleep

from appium import webdriver

'''
01：
最初级的appium的测试脚本，打开APP，并且点击元素
'''

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'd0a49989'
desired_caps['appPackage'] = 'com.browser2345'
desired_caps['appActivity'] = 'com.browser2345.BrowserActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

el = driver.find_element_by_id('com.browser2345:id/urlbar_left')
el.click()

sleep(5)
driver.quit()
