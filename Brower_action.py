from selenium import webdriver
from time import sleep
#加载浏览器驱动
driver=webdriver.Chrome()
#打开网页
driver.get('http://www.51zxw.net')
driver.maximize_window()#设置窗口最大
sleep(2)

driver.get('http://www.51zxw.net/list.aspx?cid=615')
driver.set_window_size(400,800)
driver.refresh()#刷新页面
sleep(2)

driver.back()#后退页面
sleep(2)

driver.forward()#前进
sleep(2)

driver.quit()
