from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
file_path=r"file:/Users/wangqian/Desktop/Frame.html"

driver.get(file_path)

driver.switch_to.frame('search')
driver.find_element_by_css_selector('#query').send_keys('python')
sleep(3)
driver.find_element_by_css_selector('#stb').click()
sleep(3)
driver.quit()
