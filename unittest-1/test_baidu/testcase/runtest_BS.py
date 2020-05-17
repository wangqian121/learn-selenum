from BSTestRunner import BStestRunner
import unittest
import time

test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    report_dir='./report'
    now=time.strftime('%Y-%m-%d-%H-%M-%s')
    report_name=report_dir+'/'+now+'result.html'
    with open(report_name,'w') as f:
        runner=BStestRunner(stream=f,title='test-report',discription='test-result')
        runner.run(discover)