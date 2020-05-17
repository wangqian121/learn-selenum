from selenium import webdriver
from time import sleep
dever=webdriver.Chrome()
dever.get("http://www.baidu.com")

dever.find_element_by_id("kw").send_keys("selenium我要自学网")
sleep(2)
dever.find_element_by_id('su').click()
dever.quit()
