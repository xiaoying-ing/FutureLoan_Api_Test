# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   test_login.py

@Time    :   2020/7/3 16:51

@Desc    :

'''
import unittest
from ddt import ddt, data
from TestDatas.excel_data_obtain import test_login_datas
from Common.handle_logger import myLogger
from Common.handle_requests import set_request
import json
# from pprint import pprint
#
# pprint(test_login_datas)
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        myLogger.info("==================登录模块接口测试开始==================")

    def setUp(self) -> None:
        myLogger.info("==================接口用例执行开始==================")

    @data(*test_login_datas)
    def test_login(self, cases):
        myLogger.info("==================用例{}执行开始==================".format(cases['number']))
        # myLogger.info("测试数据{}：".format(test_login_datas))
        # myLogger.info("用例描述:{}".format(cases['case_name']))
        # myLogger.info("期望结果:{}".format(cases['expect_res']))
        cases["case_name"] = cases["case_name"].replace("\n", "-")
        self.__dict__['_testMethodDoc'] = str(cases["number"]) + "-" + cases["case_name"]
        resp_login = set_request(cases["url"], cases["method"], data=cases["request_data"])
        # myLogger.info("响应数据:{}".format(resp_login.json()))
        cases['expect_res'] = json.loads(cases['expect_res'])
        myLogger.info("预期结果为：{}".format(cases['expect_res']))
        try:
            self.assertEqual(resp_login.status_code, cases['status_code'])
            self.assertEqual(resp_login.json()["code"], cases['expect_res']["code"])
            self.assertEqual(resp_login.json()["msg"], cases['expect_res']["msg"])

        except AssertionError:
            myLogger.exception("断言失败")
            raise
        myLogger.info("==================用例{}执行结束==================".format(cases['number']))

    def tearDown(self) -> None:
        myLogger.info("==================接口用例执行结束==================")

    @classmethod
    def tearDownClass(cls) -> None:
        myLogger.info("==================登录模块接口测试结束==================")