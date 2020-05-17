from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.get_screenshot_as_file(r'/Users/wangqian/Desktop/baidu.jpg')
sleep(2)

driver.get('http://51zxw.net/')
driver.get_screenshot_as_file(r'/Users/wangqian/Desktop/51xzw.png')
sleep(2)
driver.quit()
