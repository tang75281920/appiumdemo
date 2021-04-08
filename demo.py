from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'd0a49989'
desired_caps['appPackage'] = 'com.browser2345'
desired_caps['appActivity'] = 'com.browser2345.BrowserActivity'
desired_caps['noReset'] = 'true'

#desired_caps['appPackage'] = 'com.planet.light2345'
#desired_caps['appActivity'] = 'com.planet.light2345.launch.LaunchActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
sleep(10)
driver.quit()
