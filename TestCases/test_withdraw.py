# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   test_withdraw.py

@Time    :   2020/7/14 14:58

@Desc    :

'''
import unittest
from jsonpath import jsonpath
from ddt import ddt, data
from TestDatas.excel_data_obtain import test_withdraw_datas
from Common.handle_logger import myLogger
from Common.handle_requests import set_request
from Common.handle_mysql import HandleDB
from Common.handle_case_relpace_data import replace_mark_with_data, EnvData
from Common.handle_phone import get_old_phone
import json

db = HandleDB()

@ddt
class TestWithdraw(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        myLogger.info("==================提现模块接口测试开始==================")
        user, password = get_old_phone()
        response_login = set_request("member/login", "post", {"mobile_phone": user, "pwd": password})
        myLogger.info("登录的响应数据为：{}".format(response_login.json()))
        # cls.member_id = jsonpath(response_login.json(), "$..id")[0]
        # cls.token = jsonpath(response_login.json(), "$..token")[0]
        setattr(EnvData, "member_id", jsonpath(response_login.json(), "$..id")[0])
        setattr(EnvData, "token", jsonpath(response_login.json(), "$..token")[0])
        myLogger.info("登录用户id:{}\n token:{}".format(EnvData.member_id, EnvData.token))

    def setUp(self) -> None:
        myLogger.info("==================接口用例执行开始==================")

    @data(*test_withdraw_datas)
    def test_withdraw(self, cases):
        self.__dict__['_testMethodDoc'] = str(cases["number"]) + "-" + cases["case_name"]
        if cases["request_data"].find("#member_id#") != -1:
            cases = replace_mark_with_data(cases, "#member_id#", str(EnvData.member_id))

        if cases["check_sql"]:
            user_money_now = db.select_one_data(cases["check_sql"])["leave_amount"]
            myLogger.info("用户提现之前的余额为：{}".format(user_money_now))
            withdraw_money = json.loads(cases["request_data"])["amount"]
            myLogger.info("提现的金额：{}".format(withdraw_money))
            user_money_withdraw_balance = round(float(user_money_now) - float(withdraw_money), 2)
            myLogger.info("用户提现后所剩余额：{}".format(user_money_withdraw_balance))
            cases = replace_mark_with_data(cases, "#money#", str(user_money_withdraw_balance))

        response_withdraw = set_request(cases["url"], cases["method"], cases["request_data"], token=EnvData.token)
        expected = json.loads(cases["expect_res"])
        myLogger.info("期望结果：{}".format(expected))

        # 断言
        try:
            self.assertEqual(response_withdraw.json()["code"], expected["code"])
            self.assertEqual(response_withdraw.json()["msg"], expected["msg"])
            if cases["check_sql"]:
                self.assertEqual(jsonpath(response_withdraw.json(), "$..id")[0], expected["data"]["id"])
                self.assertEqual(jsonpath(response_withdraw.json(), "$..leave_amount")[0],
                                 expected["data"]["leave_amount"])
                user_money_balance = db.select_one_data(cases["check_sql"])["leave_amount"]
                myLogger.info("数据库中用户余额显示:{}".format(user_money_balance))
                self.assertEqual("{:.2f}".format(float(user_money_balance)),
                                 "{:.2f}".format(expected["data"]["leave_amount"]))

        except AssertionError:
            myLogger.info("断言失败")
            raise

    def tearDown(self) -> None:
        myLogger.info("==================接口用例执行结束==================")

    @classmethod
    def tearDownClass(cls) -> None:
        myLogger.info("==================提现模块接口测试结束==================")
