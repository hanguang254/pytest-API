import time

from HTMLTestRunner import HTMLTestRunner
import unittest

from out_put import get_local
from test_case.tianqi_test import Test_tainqi


s=unittest.TestSuite()
l=unittest.TestLoader()
s.addTest(l.loadTestsFromTestCase(Test_tainqi))

filepath= get_local.get_cwd()
# print(filepath)
Ftime=time.strftime("%Y%m%d%H%M%S",time.localtime())
filename=filepath+r"\report_test\报告"+Ftime+".html"
with open(filename,'wb' ) as f:
    test=HTMLTestRunner(stream=f,
                         verbosity=2, #详细程度
                         title='测试报告',
                          description="接口测试报告",
                          tester="尹乐")
    test.run(s)
