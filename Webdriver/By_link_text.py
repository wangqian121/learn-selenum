from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()

driver.get('http://www.51zxw.net')
driver.find_element_by_link_text("程序设计").click()#文本链接
sleep(2)
driver.find_element_by_link_text("Selenium").click()#全部匹配
sleep(2)
driver.find_element_by_partial_link_text("课程概述").click()#部分匹配