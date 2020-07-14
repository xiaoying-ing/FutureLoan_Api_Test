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
from Common.handle_conf import red_conf
import json
from Common.handle_logger import myLogger


def set_request(url, method, data=None, params_format="json", token=None):
    '''
    2、动态发送请求:
    1.1 如果传入"POST"，发送post请求
    1.2 如果传入"GET"， 发送get请求
    1.3 考虑token鉴权
    :param params_format: 请求数据的格式---->application/x-www-form-urlencoded为data，类型为dict；application/json为就json
                          类型为dict
    :param url:请求地址
    :param method:请求方式
    :param data:请求数据
    :param token:token鉴权
    :return:请求后服务器返回的响应
    '''
    resp = None
    headers = __handle_headers(token)
    url = __pre_url(url)
    data = __per_data(data)
    myLogger.info("请求头为：{}".format(headers))
    myLogger.info("请求方法为：{}".format(method))
    myLogger.info("请求url为：{}".format(url))
    myLogger.info("请求数据为：{}".format(data))
    method = method.upper()
    if method == "POST":
        if params_format == "json":
            resp = requests.post(url, json=data, headers=headers)
        else:
            resp = requests.post(url, data=data, headers=headers)
    elif method == "GET":
        resp = requests.get(url, data, headers=headers)
    myLogger.info("响应状态码：{}".format(resp.status_code))
    myLogger.info("响应数据：{}".format(resp.json()))
    return resp


def __handle_headers(token=None):
    '''
    1、动态获取请求头：
    1.1 如果没有token，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type":"application/json"}
    1.2 如果传入token参数，请求头为headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
                                            "Authorization": "Bearer{}".format(token)}
    :param token:如果需要token鉴权，传入token参数
    :return:处理之后的请求头
    '''
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def __pre_url(url):
    '''
    拼接接口的url地址。
    :param url:读取的excel里面的url
    :return:
    '''
    base_url = red_conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


def __per_data(data):
    '''
    处理读取出来的测试用例数据
    :param data:
    :return:
    '''
    if data is not None and isinstance(data, str):
        data = json.loads(data)
    elif data is not None and data is int:
        data = str(data)
    return data


if __name__ == '__main__':
    register_url = "member/register"
    datas = {"mobile_phone":"18770915781","pwd":"19960916","type": "1", "reg_name": "小音"}
    res = set_request(register_url, "POST", datas)
    print(res.json())

