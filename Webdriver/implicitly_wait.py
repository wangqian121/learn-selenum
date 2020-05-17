from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)
driver.implicitly_wait(5)#隐式等待设定5s
#检索搜索框是否存在
try:
    print(ctime())
    driver.find_element_by_css_selector('#kw').send_keys('python')
    driver.find_element_by_css_selector('#su1').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(3)
driver.quit()