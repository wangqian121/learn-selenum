from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get('http://www.51zxw.net')
print(driver.title)
sleep(3)

driver.get('http://www.baidu.com')
print("执行完成")
driver.quit()
