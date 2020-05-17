from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com/')
sleep(2)
driver.find_element_by_css_selector('#kw').send_keys('selenium')
elemet=WebDriverWait(driver,5,0.5).until(ec.presence_of_element_located((By.ID,'su11')))
elemet.click()
sleep(3)
driver.quit()
