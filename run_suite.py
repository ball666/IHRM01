# 使用testrunner生成测试报告
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from app import BASE_DIR
# 实例化suite对象


suite = unittest.TestSuite()
# 添加测试用例到测试套件
dir = BASE_DIR+"/script"
suite.addTest(unittest.TestLoader().discover(dir))
# 设置文件格式
filename = BASE_DIR + "/report/report.html"
# 打开测试报告文件
with open(filename,'wb') as f :
    # 实例化runner对象
    runner = HTMLTestRunner(stream=f,verbosity=2,title="Tpshop商城接口测试报告",description="win10-Chrome80")
    # 运行测试套件
    runner.run(suite)