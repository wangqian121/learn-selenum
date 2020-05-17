import unittest
from selenium import webdriver
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #设置隐式等待
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")
    def test_baidu(self):
        #driver=self.driver
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id("kw").send_keys("selenium自学网")
        self.driver.find_element_by_id('su').click()
        sleep(3)
        title=self.driver.title
        self.assertEqual(title,'selenium自学网_百度搜索')
        self.driver.find_element_by_partial_link_text("Selenium自动化").click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()


