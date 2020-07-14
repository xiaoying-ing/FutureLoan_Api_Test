# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   test_register.py

@Time    :   2020/7/3 9:56

@Desc    :

'''
import unittest
from ddt import ddt, data
from TestDatas.excel_data_obtain import test_register_datas
from Common.handle_logger import myLogger
from Common.handle_requests import set_request
from Common.handle_mysql import HandleDB
from Common.handle_case_relpace_data import replace_mark_with_data
from Common.handle_phone import get_new_phone
import json

db = HandleDB()
REPLACE_DATA = "#phone#"

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        myLogger.info("==================注册模块接口测试开始==================")

    def setUp(self) -> None:
        myLogger.info("==================接口用例执行开始==================")

    @data(*test_register_datas)
    def test_register(self, cases):
        case_info = cases['case_name'].replace("\n", "--")
        myLogger.info("==================用例{}:{}执行开始==================".format(cases["number"], case_info))
        # myLogger.info("测试数据{}：".format(test_register_datas))
        if cases["request_data"].find("#phone#") != -1:
            new_phone = get_new_phone()
            cases = replace_mark_with_data(cases, REPLACE_DATA, new_phone)
        expected = json.loads(cases["expect_res"])
        self.__dict__['_testMethodDoc'] = str(cases["number"]) + "-" + case_info
        resp = set_request(cases['url'], cases['method'], data=cases["request_data"])
        myLogger.info("期望结果：{}".format(expected))
        try:
            self.assertEqual(resp.status_code, cases['status_code'])
            self.assertEqual(resp.json()["code"], expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])
            if cases["check_sql"]:
                check_result = db.select_one_data(cases["check_sql"])
                self.assertIsNotNone(check_result)
        except AssertionError:
            myLogger.exception("断言失败")
            raise
        myLogger.info("==================用例结束==================")

    def tearDown(self) -> None:
        myLogger.info("==================接口用例执行结束==================")

    @classmethod
    def tearDownClass(cls) -> None:
        myLogger.info("==================注册模块接口测试结束==================")


