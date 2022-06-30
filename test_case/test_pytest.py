import os
import allure
import pytest
import requests
from pytest_html.extras import json
from common import excel_write
from common import basepage, get_local, excel
from data import get_local_save


filepath_save=get_local_save.get_cwd()
filepath=get_local.get_cwd() #获取excel绝对路径
test_data=excel.PlayExcel(filepath+r"\1.xlsx","test").read_all()   #读取excel


@allure.feature("数据驱动接口自动化")
class Test_demo1:

    def setup_class(self):  #任何用例首先执行
        self.log=basepage.BasePage().get_log()
        self.log.info("--------------------pytest--------------------")
        self.list=[]  #实例化一个列表
    def teardown_class(self): #执行玩用例，在执行
        self.log.info("--------------------执行完成--------------------")


    @allure.story("查询成功")
    @pytest.mark.run(order=1)  #排序1，优先执行1
    @pytest.mark.parametrize('url,data,ex',[*test_data])
    def test_API(self,url,data,ex):
        try:
            # ex="查询成功"
            edata=eval(data)
            # result=requests.get("https://way.jd.com/he/freeweather",
            #                     {"appkey":"7b95369de74f07e957c9fa01f235748f","city":"长沙"}).text
            self.log.info("请求地址：{}".format(url))
            self.log.info("请求参数：{}".format(edata))
            self.log.info("预期结果：{}".format(ex))
            self.log.info("--------------------正在获取请求--------------------")
            sec=requests.get(url).elapsed.total_seconds() #响应时间
            result=requests.get(url,edata).text  #参数化

            #将返回值加入一个列表
            self.list.append(result)
            #将返回值写入excel表格
            excel_write.Write_excel(filepath_save,r"\返回值.xlsx","返回值",self.list).write_result()
            # self.log.info("返回响应：{}".format([result]))

            assert ex in result
            self.log.info("-------------查询成功，响应时间：{}秒----------------".format([sec]))
            self.log.info("---------------------------------------分割线----------------------------------------")
        except AssertionError as A:
            self.log.info("--------------------预期结果不在实际结果中--------------------")
            self.log.error(A)
        except Exception as E:
            self.log.error(E)

if __name__ == '__main__':
    # pytest.main(["-s","test_pytest.py"])

    result_dir = "../out_put/json"  #json存储位置
    report_dir = "../out_put/report_test"  #报告存储位置
    # pytest.main() 相当于执行pytest命令
    pytest.main(["-sv", "--alluredir=%s" % result_dir, "--clean-alluredir", "test_pytest.py"])
    os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))
