# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   test_recharge.py

@Time    :   2020/7/22 14:54

@Desc    :

'''
# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   test_recharge.py

@Time    :   2020/7/10 10:31

@Desc    :
        充值模块测试用例
        1、动态替换测试用例数据：
            1.1 替换 #member_id# 为cls.id
            1.2 查询数据库，替换 #money# ：为 充值金额（amount） + 余额 （查询数据库获得，为Decimal类型数据，使用SQL语言处理）
        2、发送请求
        3、断言
        :param cases: 测试数据，DDT传入
        :return:
'''
import unittest
from jsonpath import jsonpath
from ddt import ddt, data
from TestDatas.excel_data_obtain import test_recharge_datas
from Common.handle_logger import myLogger
from Common.handle_requests import set_request
from Common.handle_mysql import HandleDB
from Common.handle_case_relpace_data import replace_case_by_reglur, EnvData, clear_EnvData_attrs
from Common.handle_phone import get_old_phone
import json

db = HandleDB()
# print(type(test_recharge_datas[0]["expect_res"]))

@ddt
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        clear_EnvData_attrs()
        myLogger.info("==================充值模块接口测试开始==================")
        user, password = get_old_phone()
        response_login = set_request("member/login", "post", {"mobile_phone": user, "pwd": password})
        myLogger.info("登录的响应数据为：{}".format(response_login.json()))
        setattr(EnvData, "member_id", str(jsonpath(response_login.json(), "$..id")[0]))
        setattr(EnvData, "token", jsonpath(response_login.json(), "$..token")[0])
        # cls.member_id = jsonpath(response_login.json(), "$..id")[0]
        # cls.token = jsonpath(response_login.json(), "$..token")[0]
        myLogger.info("登录用户id:{}\n token:{}".format(EnvData.member_id, EnvData.token))

    def setUp(self) -> None:
        myLogger.info("==================接口用例执行开始==================")

    @data(*test_recharge_datas)
    def test_recharge(self, cases):
        self.__dict__['_testMethodDoc'] = str(cases["number"]) + "-" + cases["case_name"]
        if cases["request_data"].find("#member_id#") != -1:
            cases = replace_case_by_reglur(cases)
            # print(cases)

        if cases["check_sql"]:
            user_money_before = db.select_one_data(cases["check_sql"])["leave_amount"]
            myLogger.info("充值之前用户余额：{}".format(user_money_before))
            recharge_money = json.loads(cases["request_data"])["amount"]
            myLogger.info("充值金额为：{}".format(recharge_money))
            user_money_after = round(float(user_money_before) + recharge_money, 2)    # 获取这个值是为了替换用例中的期望数据
            myLogger.info("预期充值之后的金额为：{}".format(user_money_after))
            setattr(EnvData, "money", str(user_money_after))
            cases = replace_case_by_reglur(cases)
        response_recharge = set_request(cases["url"], cases["method"], cases["request_data"], token=EnvData.token)
        # user_money = db.select_one_data(cases["check_sql"])["leave_amount"]
        # myLogger.info("充值之后。。。。：{}".format(user_money))
        expected = json.loads(cases["expect_res"])
        myLogger.info("期望结果为：{}".format(expected))

        # 断言
        try:
            self.assertEqual(response_recharge.json()["code"], expected["code"])
            self.assertEqual(response_recharge.json()["msg"], expected["msg"])
            if cases["check_sql"]:
                self.assertEqual(response_recharge.json()["data"]["id"], expected["data"]["id"])
                self.assertEqual(response_recharge.json()["data"]["leave_amount"], expected["data"]["leave_amount"])
                user_recharge_after_money = db.select_one_data(cases["check_sql"])["leave_amount"]
                myLogger.info("充值之后用余额：{}".format(user_recharge_after_money))
                self.assertEqual("{:.2f}".format(float(user_recharge_after_money)), "{:.2f}".format(expected["data"]
                                                                                                    ["leave_amount"]))
        except AssertionError:
            myLogger.info("断言失败")
            raise

    def tearDown(self) -> None:
        if hasattr(EnvData,"money"):
            delattr(EnvData,"money")
        myLogger.info("==================接口用例执行结束==================")

    @classmethod
    def tearDownClass(cls) -> None:
        myLogger.info("==================充值模块接口测试结束==================")


