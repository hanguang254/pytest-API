import pytest
import subprocess

if __name__ == '__main__':
    case=[r"D:\接口自动化\test_case\test_pytest.py"]  #用例文件
    cmmder=['-s','-q','-v','--alluredir=../out_put/json','--clean-alluredir']     #打印格式，以及json文件存储地址
    case.extend(cmmder)
    pytest.main(case)   #执行用例
    subprocess.Popen("allure generate ../out_put/json -o ../out_put/report_test --clean",shell=True) #保存位置
