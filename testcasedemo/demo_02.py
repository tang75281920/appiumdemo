from appium import webdriver

"""
02：
使用Appium Desktop录制的脚本：
使用小米系统拨号，拨打10086
博客：https://blog.csdn.net/tt75281920/article/details/115646935?spm=1001.2014.3001.5501
"""

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "d0a49989"
caps["appPackage"] = "com.android.contacts"
caps["appActivity"] = "com.android.contacts.activities.TwelveKeyDialer"
caps["noReset"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_accessibility_id("一")
el1.click()
el2 = driver.find_element_by_accessibility_id("零")
el2.click()
el2.click()
el3 = driver.find_element_by_accessibility_id("八")
el3.click()
el4 = driver.find_element_by_accessibility_id("六")
el4.click()
el5 = driver.find_element_by_accessibility_id("拨打电话")
el5.click()

driver.quit()
