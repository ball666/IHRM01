# 封装部门的接口
import requests
class DepartmentApi():

    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.add_url = "http://182.92.81.159/api/company/department"
        self.url =  "http://182.92.81.159/api/company/department/"
    # 封装登录的接口
    def login(self,mobile,password):
        json_data = {"mobile":mobile,"password":password}
        return requests.post(self.login_url,json=json_data)

    # 封装添加部门的接口
    def add_department(self,name,code,manager,introduce,headers):
        json_data = {"name":name,"code":code,"manager":manager,"introduce":introduce,"pid":""}
        return requests.post(self.add_url,json = json_data,headers = headers)

    # 封装查询部门的接口
    def find_department(self,dep_id,headers):
        return requests.get(self.url + dep_id,headers=headers)

    # 封装修改部门的接口
    def update_department(self,name,code,dep_id,headers):
        json_data = {"name":name,"code":code}
        return requests.put(self.url+dep_id,json = json_data,headers = headers)

    # 封装删除部门的接口
    def delete_department(self,dep_id,headers):
        return requests.delete(self.url + dep_id, headers=headers)




