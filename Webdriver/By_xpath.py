from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
# 绝对定位
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[1]/div/form/span[1]/input").send_keys('我要自学网')
# 相对定位
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("selenium")
driver.find_element_by_xpath('//input[@id="su"]').click()