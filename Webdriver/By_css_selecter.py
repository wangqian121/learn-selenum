from selenium import webdriver
from time import sleep
drive=webdriver.Chrome()
drive.get("http://www.baidu.com")
# drive.find_element_by_css_selector('#kw').send_keys('selenium')#通过id定位
#drive.find_element_by_css_selector('.s_ipt').send_keys('selenium')#通过class定位
drive.find_element_by_css_selector('[autocomplete="off"]').send_keys("selenium")#通过属性
sleep(2)
drive.find_element_by_id('su').click()
sleep(2)
drive.quit()

