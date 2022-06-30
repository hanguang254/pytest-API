import unittest
import requests
from common import basepage
from ddt import ddt,unpack,data
from common import get_local
from common import excel

filepath=get_local.get_cwd() #获取excel绝对路径
test_data=excel.PlayExcel(filepath+r"\2.xlsx","test").read_all()   #读取excel

@ddt
class Test_tainqi(unittest.TestCase):

    @classmethod
    def setUpClass(slef):
        slef.log = basepage.BasePage().get_log()
        slef.log.info("----------正在启动------------")
    @classmethod
    def tearDownClass(slef):
        slef.log.info("-----------测试完毕——-------")
        pass
    @data(*test_data)
    @unpack
    def test_get_tianqi(slef,url,data,ex):   #通过excel 传入请求地址，参数，预期结果
        slef.log.info("----------正在获取响应---------")
        try:
            # ex="查询成功"
            edata=eval(data)  #excel默认输出为字符串，输出格式为字典格式
            result=requests.get(url,edata).text
            sec=requests.get(url).elapsed.total_seconds()   #获取响应时间
            slef.assertIn(ex,result)
            slef.log.info("---响应时间为:{}---------".format(sec))
            slef.log.info("------------测试成功-----------")
        except AssertionError as a:  #断言异常
            slef.log.info("----------断言出现异常----------")
            slef.log.error("返回值为：{}".format(result))
        except Exception as e:
            slef.log.error(e)

