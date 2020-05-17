from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://51zxw.net')
# 将滚动条拖到最底部
js = 'var action=document.documentElement.scrollTop=10000'
driver.execute_script(js)
sleep(5)
js = 'var action=document.documentElement.scrollTop=0'
driver.execute_script(js)
sleep(5)
driver.quit()
