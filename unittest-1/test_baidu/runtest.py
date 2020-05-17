import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir='./testcase'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    # runner=unittest.TextTestRunner()
    # runner.run(discover)
    #存放报告的文件夹
    report_dir='./report'
    #报告命名时间格式化
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    #报告文件完整路径
    report_name=report_dir+'/'+now+'result.html'
    #打开文件在报告文件写入测试结果
    with open(report_name,'w') as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='Test Report',description='Test case')
        runner.run(discover)