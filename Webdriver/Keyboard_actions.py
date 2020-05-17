from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector('#kw').send_keys('python')
sleep(3)
#全选
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
#复制或剪切
sleep(3)
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')

#driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')
sleep(3)
driver.get('http://www.sogou.com')
#粘贴
driver.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL,'v')
sleep(3)
driver.find_element_by_css_selector('#stb').click()
sleep(3)
driver.quit()