# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_requests.py

@Time    :   2020/6/30 14:58

@Desc    :

'''
'''
封装---处理requests请求
1、动态获取请求头：
    1.1 如果没有token，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type":"application/json"}
    1.2 如果传入token参数，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json", 
                                            "Authorization": "Bearer{}".format(token)}

2、动态发送请求:
    1.1 如果传入"POST"，发送post请求
    1.2 如果传入"GET"， 发送get请求
    1.3 考虑token鉴权
'''
import requests


class handle_requests:
    def __init__(self, url, method, request_param, token=None, requests_format="json"):
        '''
        :param url: 请求地址
        :param method: 请求方式
        :param request_param: 请求参数
        :param token: token
        :param requests_format:请求数据格式
        '''
        self.url = url
        self.method = method
        self.requset_param = request_param
        self.token = token
        self.requset_format = requests_format

    def __handle_headers(self):
        '''
        1、动态获取请求头：
        1.1 如果没有token，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type":"application/json"}
        1.2 如果传入token参数，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
                                                "Authorization": "Bearer{}".format(token)}
        :param token:如果需要token鉴权，传入token参数
        :return:处理之后的请求头
        '''
        headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = "Bearer {}".format(self.token)
        return headers

    def set_request_token(self):   # url, method, data=None, token=None
        '''
        2、动态发送请求:
        1.1 如果传入"POST"，发送post请求
        1.2 如果传入"GET"， 发送get请求
        1.3 考虑token鉴权
        :param url:请求地址
        :param method:请求方式
        :param data:请求数据
        :param token:token鉴权
        :return:请求后服务器返回的响应
        '''
        resp = None
        headers_data = self.__handle_headers()
        method = self.method.upper()
        if method == "POST":
            if self.requset_format == "json":
                resp = requests.post(self.url, json=self.requset_param, headers=headers_data)
            else:
                resp = requests.post(self.url, data=self.requset_param, headers=headers_data)
        elif method == "GET":
            resp = requests.get(self.url, headers=headers_data)
        return resp

    def set_request_cookies(self):
        resp = None
        session_login = requests.Session()
        headers_data = self.__handle_headers()
        method = self.method.upper()
        if method == "POST":
            resp = session_login.post(self.url, json=self.requset_param, headers=headers_data)
        elif method == "GET":
            resp = requests.get(self.url, headers=headers_data)
        return resp


