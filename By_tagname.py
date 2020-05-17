from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http:www.51zxw.net')
#获取页面第一个input
driver.find_element_by_tag_name("input").send_keys("Selenium")
#获取页面所有input
#driver.find_elements_by_tag_name("input")[0].send_keys("Selenium")
sleep(2)
driver.quit()