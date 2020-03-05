# 用于登录
import unittest,logging
import requests
from api.login_api import LoginApi
# 定义测试类
from utils import assert_common


class Login(unittest.TestCase):
    # 定义初始值和销毁值
    def setUp(self) -> None:
        self.login_api = LoginApi()
    def tearDown(self) -> None:
        pass

    # 定义测试方法
    # 登录成功
    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        # 打印结果
        logging.info("登录成功的信息为{}".format(response.json()))
        # 断言
        assert_common(self,response,200,True,10000,"操作成功")

    # 用户名不存在
    def test02_username_no_exist(self):
        response = self.login_api.login("13800000454","123456")
        # 打印结果
        logging.info("用户名不存在的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 密码错误
    def test03_password_error(self):
        response = self.login_api.login("13800000002","8888")
        # 打印结果
        logging.info("密码错误的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 无参数
    def test04_no_params(self):
        response = requests.post("http://182.92.81.159/api/sys/login")
        # 打印结果
        logging.info("无参数的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,99999,"抱歉，系统繁忙，请稍后重试")

    # 用户名为空
    def test05_username_is_empty(self):
        response = self.login_api.login("","8888")
        # 打印结果
        logging.info("用户名为空的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 密码为空
    def test06_password_is_empty(self):
        response = self.login_api.login("13800000002","")
        # 打印结果
        logging.info("密码为空的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 缺少mobile参数
    def test07_no_mobile(self):
        response = self.login_api.login_params({"password":"123456"})
        #         # 打印结果
        logging.info("缺少mobile参数的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 缺少password参数
    def test08_no_password(self):
        response = self.login_api.login_params({"mobile":"13800000002"})
        #         # 打印结果
        logging.info("缺少password参数的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response,200,False,20001,"用户名或密码错误")

    # 多参
    def test09_no_password(self):
        response = self.login_api.login_params({"mobile":"13800000002","password":"123456","hhh":"0000"})
        # 打印结果
        logging.info("多参的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

    # 错误参数
    def test10_params_error(self):
        response = self.login_api.login_params({"mobile":"13800000002","pass":"123456"})
        #         # 打印结果
        logging.info("错误参数的信息为{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

