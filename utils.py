import os

import pymysql
import json

# 封装通用断言函数
from app import BASE_DIR

def assert_common(self,response,http_code,success,code,message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 定义一个连接数据库的工具类
class DBUtils():
    # 初始化
    def __init__(self,host = "182.92.81.159", user = "readuser",password = "iHRM_user_2019",database = "ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 进入with时会自动运行的代码
    def __enter__(self):
        # 创建连接
        self.conn = pymysql.connect(host = self.host,user = self.user,password = self.password,database = self.database)
        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 退出with时自动关闭
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()



# 获取登录数据的方法
def get_login_data():
    with open(BASE_DIR+"/data/login_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        data_list = []
        for i in json_data:
            mobile = i.get("mobile")
            password = i.get("password")
            http_code = i.get("http_code")
            success = i.get("success")
            code = i.get("code")
            message = i.get("message")
            data_list.append((mobile,password,http_code,success,code,message))

        return data_list

# 获取添加员工模块数据的方法
def get_add_data():
    with open(BASE_DIR+"/data/emp_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        add_list = []
        add_emp_data = json_data.get("add_emp")

        username = add_emp_data.get("username")
        password = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        add_list.append((username,password,http_code,success,code,message))
        return add_list

# 获取查询员工模块数据的方法
def get_find_data():
    with open(BASE_DIR+"/data/emp_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        find_list = []
        find_emp_data = json_data.get("query_emp")

        http_code = find_emp_data.get("http_code")
        success = find_emp_data.get("success")
        code = find_emp_data.get("code")
        message = find_emp_data.get("message")
        find_list.append((http_code,success,code,message))
        return find_list

# 获取修改员工模块数据的方法
def get_update_data():
    with open(BASE_DIR+"/data/emp_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        update_list = []
        update_emp_data = json_data.get("modify_emp")

        username = update_emp_data.get("username")
        http_code = update_emp_data.get("http_code")
        success = update_emp_data.get("success")
        code = update_emp_data.get("code")
        message = update_emp_data.get("message")
        update_list.append((username,http_code,success,code,message))
        return update_list

# 获取删除员工模块数据的方法
def get_delete_data():
    with open(BASE_DIR+"/data/emp_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        delete_list = []
        delete_emp_data = json_data.get("delete_emp")

        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        delete_list.append((http_code,success,code,message))
        return delete_list

# 定义一个获取添加部门数据的方法
def add_dep_data():
    with open(BASE_DIR+"/data/dep_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        add_dep_list = []
        add_dep_data = json_data.get("add_dep")

        name = add_dep_data.get("name")
        code = add_dep_data.get("code")
        manager = add_dep_data.get("manager")
        introduce = add_dep_data.get("introduce")
        http_code = add_dep_data.get("http_code")
        success = add_dep_data.get("success")
        code1 = add_dep_data.get("code1")
        message = add_dep_data.get("message")
        add_dep_list.append((name,code,manager,introduce,http_code,success,code1,message))
        return add_dep_list

# 定义一个获取查找部门数据的方法
def find_dep_data():
    with open(BASE_DIR+"/data/dep_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        find_dep_list = []
        find_dep_data = json_data.get("find_dep")

        code = find_dep_data.get("code")
        http_code = find_dep_data.get("http_code")
        success = find_dep_data.get("success")
        code1 = find_dep_data.get("code1")
        message = find_dep_data.get("message")
        find_dep_list.append((code,http_code,success,code1,message))
        return find_dep_list

# 定义一个获取修改部门数据的方法
def update_dep_data():
    with open(BASE_DIR+"/data/dep_data.json",encoding='utf-8') as f:
        json_data = json.load(f)
        update_dep_list = []
        update_dep_data = json_data.get("update_dep")

        name = update_dep_data.get("name")
        code = update_dep_data.get("code")
        http_code = update_dep_data.get("http_code")
        success = update_dep_data.get("success")
        code1 = update_dep_data.get("code1")
        message = update_dep_data.get("message")
        update_dep_list.append((name,code,http_code,success,code1,message))
        return update_dep_list


# 定义一个获取删除部门数据的方法
def delete_dep_data():
    with open(BASE_DIR + "/data/dep_data.json", encoding='utf-8') as f:
        json_data = json.load(f)
        delete_dep_list = []
        delete_dep_data = json_data.get("delete_dep")


        http_code = delete_dep_data.get("http_code")
        success = delete_dep_data.get("success")
        code1 = delete_dep_data.get("code1")
        message = delete_dep_data.get("message")
        delete_dep_list.append((http_code, success, code1, message))
        return delete_dep_list


