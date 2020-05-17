from LoginPage import *
from selenium import webdriver

driver=webdriver.Chrome()
username='12345'
password='12345'
test_user_login(driver,username,password)
sleep(3)
driver.quit()