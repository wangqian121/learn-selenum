from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)
driver.find_element_by_class_name("s_ipt").send_keys("我要自学网")
sleep(2)

driver.find_element_by_id('su').click()
sleep(2)
driver.quit()