# 用于登录参数化代码
import unittest,logging
import requests
from api.login_api import LoginApi
from parameterized import parameterized
from utils import assert_common, get_login_data

data_list = get_login_data()
# 定义测试类
class Login(unittest.TestCase):
    # 定义初始值和销毁值
    def setUp(self) -> None:
        self.login_api = LoginApi()
    def tearDown(self) -> None:
        pass

    @parameterized.expand(data_list)
    # 定义测试方法
    # 登录用例
    def test_login(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        # 打印结果
        logging.info("登录的信息为{}".format(response.json()))
        # 断言
        assert_common(self,response,http_code,success,code,message)
