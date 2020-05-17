from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()#最大化
driver.find_element_by_css_selector('#kw').send_keys('python')
sleep(3)
element=driver.find_element_by_css_selector('#kw')
#双击操作
ActionChains(driver).double_click(element).perform()
sleep(3)
#右击操作
ActionChains(driver).context_click(element).perform()
sleep(3)
#悬停操作
abrove=driver.find_element_by_css_selector('.pf')
ActionChains(driver).move_to_element(abrove).perform()
sleep(3)
driver.quit()


