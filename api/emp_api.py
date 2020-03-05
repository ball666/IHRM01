# 封装员工登录/添加员工/查询员工/删除员工/修改员工的接口
import requests
class employee_api():
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.add_url = "http://182.92.81.159/api/sys/user"
        self.url = "http://182.92.81.159/api/sys/user/"
    # 封装登录的接口
    def login(self,mobile,password):
        json_data = {"mobile":mobile,"password":password}
        return requests.post(self.login_url,json=json_data)

    # 封装添加员工的接口
    def add_employee(self,username,mobile,headers):
        json_data = {"username": username,
                       "mobile": mobile,
                       "timeOfEntry": "2019-07-01",
                       "formOfEmployment": 1,
                       "departmentName": "开发部",
                       "departmentId": "1066240656856453120"}
        return requests.post(self.add_url ,json=json_data,headers=headers)

    # 封装查询员的接口
    def find_employee(self,emp_id,headers):

        return requests.get(self.url+ emp_id,headers = headers)

    # 封装修改员工的接口
    def update_employee(self,emp_id,username,headers):
        json_data = {"username":username}
        return requests.put(self.url+ emp_id,json = json_data, headers=headers)

    # 封装删除员工的接口
    def delete_employee(self,emp_id,headers):
        return requests.delete(self.url+ emp_id,headers=headers)



