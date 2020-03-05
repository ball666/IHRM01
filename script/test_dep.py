# 用于对部门的增删改查
import logging
import unittest
from utils import assert_common, DBUtils, add_dep_data, find_dep_data, update_dep_data, delete_dep_data
import  api
import app
from api.dep_api import DepartmentApi
from parameterized import parameterized
# 定义测试类
class TestDepartment(unittest.TestCase):

    # 定义初始化
    def setUp(self) -> None:
        self.dep_api = DepartmentApi()

    #定义 测绘方法
    # 调用登录接口
    def test01_login(self):
        response = self.dep_api.login("13800000002","123456")
        # 打印请求体,获取令牌
        logging.info("部门模块登录的接口为{}:".format(response.json()))
        token = "Bearer "+response.json().get("data")
        logging.info("令牌为{}:".format(token))
        # 设置请求头
        headers = {"Content-Type":"application/json","Authorization":token}
        app.HEADERS = headers

    # 调用添加部门接口
    @parameterized.expand(add_dep_data)
    def test02_add_dep(self,name,code,manager,introduce,http_code,success,code1,message):
        response_add = self.dep_api.add_department(name,code,manager,introduce,app.HEADERS)
        # 打印响应体
        logging.info("添加部门接口为{}".format(response_add.json()))
        # 断言
        assert_common(self,response_add,http_code,success,code1,message)

    # 调用查询部门接口
    @parameterized.expand(find_dep_data)
    def test03_find_dep(self,code,http_code,success,code1,message):
        # 查询数据库里的ID,放在全局变量里
        with DBUtils() as db:
            sql = "select id from `co_department` where `code` = '{}';".format(code)
            db.execute(sql)
            data = db.fetchone()
            app.DEPID = data[0]
        # 查询部门
        response_find = self.dep_api.find_department(app.DEPID,app.HEADERS)
        # 打印响应体
        logging.info("查询部门接口为{}".format(response_find.json()))
        # 断言
        assert_common(self,response_find,http_code,success,code1,message)

    # 调用修改部门接口
    @parameterized.expand(update_dep_data)
    def test04_update_dep(self,name,code,http_code,success,code1,message):
        # 修改部门
        response_update = self.dep_api.update_department(name,code,app.DEPID,app.HEADERS)
        # 打印响应体
        logging.info("修改部门接口为{}".format(response_update.json()))
        # 查询数据库里的ID,放在全局变量里
        with DBUtils() as db:
            sql = "select id from `co_department` where `code` = '{}';".format(code)
            db.execute(sql)
            data = db.fetchone()
            app.DEPID = data[0]
        # 断言
        assert_common(self,response_update,http_code,success,code1,message)

    # 调用删除部门接口
    @parameterized.expand(delete_dep_data)
    def test05_delete_dep(self,http_code, success, code1, message):
        # 删除部门
        response_del = self.dep_api.delete_department(app.DEPID,app.HEADERS)
        # 打印响应体
        logging.info("删除部门接口为{}".format(response_del.json()))
        # 断言
        assert_common(self,response_del,http_code,success,code1,message)
