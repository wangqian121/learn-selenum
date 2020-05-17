from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.51zxw.net/List.aspx?cid=615')
# 获取窗口句柄
driver_index = driver.current_window_handle
driver.find_element_by_partial_link_text('2-2').click()
sleep(3)
driver.switch_to.window(driver_index)
driver.find_element_by_partial_link_text('2-4').click()
sleep(3)
driver.quit()
