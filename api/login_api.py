# 封装登录的接口
import requests
class LoginApi():
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
    # 封装登录的接口
    def login(self,mobile,password):
        json_data = {"mobile":mobile,"password":password}
        return requests.post(self.login_url,json=json_data)

    # 封装库使用少参 多参 错误参的登录接口
    def login_params(self,json_data):
        return requests.post(self.login_url,json = json_data)
