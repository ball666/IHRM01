# 用户员工的增删改查
# 导包
import logging,unittest,requests
import pymysql
import app
from api.emp_api import employee_api
from utils import assert_common, DBUtils, get_add_data, get_find_data, get_update_data, get_delete_data
from parameterized import parameterized

# 创建测试类
class TestEmployee(unittest.TestCase):
    # 创建初始化和销毁
    def setUp(self) -> None:
        self.login_api = employee_api()
    def tearDown(self) -> None:
        pass

    # 登录
    def test01_login_success(self):
        # 调用登录接口
        response = self.login_api.login("13800000002","123456")
        logging.info("员工模块的登录接口为:{}".format(response.json()))
        # 获取接口令牌并打印
        token = "Bearer "+response.json().get("data")
        logging.info("取出的令牌为:{}".format(token))
        # 设置请求头
        headers = {"Content-Type":"application/json","Authorization":token}
        app.HEADERS = headers


    # 添加员工
    @parameterized.expand(get_add_data)
    def test02_add_emp(self,username,mobile,http_code,success,code,message):
        # 调用添加员工接口
        response_add_emp = self.login_api.add_employee(username, mobile, app.HEADERS)
        logging.info("添加员工响应体为{}:".format(response_add_emp.json()))
        # 断言
        assert_common(self, response_add_emp, http_code,success, code, message)
        # 保存id,以便查询和修改使用,打印一下看下会不会有有错
        app.EMPID = response_add_emp.json().get("data").get("id")
        logging.info("id值为:{}".format(app.EMPID))



    # 查询员工
    @parameterized.expand(get_find_data)
    def test03_find_emp(self,http_code,success,code,messag):
        # 调用查询员工接口
        response_find_emp = self.login_api.find_employee(app.EMPID, app.HEADERS)
        logging.info("查询员工结果为:{}".format(response_find_emp.json()))
        # 断言
        assert_common(self, response_find_emp, http_code, success, code, messag)

    # 修改员工
    @parameterized.expand(get_update_data)
    def test04_update_emp(self,username,http_code,success,code,message):
        # 调用修改员工接口
        response_update_emp = self.login_api.update_employee(app.EMPID, username, app.HEADERS)
        logging.info("修改员工结果为:{}".format(response_update_emp.json()))

        # 查询数据库
        # 创建数据路连接
        with DBUtils() as db:
            # 查询
            sql = "select username from bs_user where id = {};".format(app.EMPID)
            db.execute(sql)
            result = db.fetchone()
            logging.info("查询的结果为{}".format(result))
            # 断言数据库查询语句
            self.assertEqual(username,result[0])


            # 断言
            assert_common(self, response_update_emp, http_code, success, code, message)

    # 删除员工
    @parameterized.expand(get_delete_data)
    def test05_delete_emp(self,http_code,success,code,message):
        # 调用删除员工接口
        response_delete_emp = self.login_api.delete_employee(app.EMPID, app.HEADERS)
        logging.info("删除员工结果为:{}".format(response_delete_emp.json()))
        # 断言
        assert_common(self, response_delete_emp, http_code, success, code,message)


