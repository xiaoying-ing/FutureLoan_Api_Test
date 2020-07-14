# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   data_obtain.py

@Time    :   2020/7/3 11:20

@Desc    :

'''
from Common.handle_excel import HandleExcel
from Common.handle_path import test_datas_dir
from pprint import pprint
import os


class read_test_datas:
    def __init__(self, table_name, sheet_name):
        self.sheet_names = sheet_name
        self.table_name = table_name

    def obtain_datas(self):
        case_path = os.path.join(test_datas_dir, self.table_name)
        case_datas = HandleExcel(case_path, self.sheet_names)
        case_all_datas = case_datas.read_test_cases_datas()
        case_datas.close_file()
        return case_all_datas


test_table_name = "前程贷-注册_登录_充值接口用例设计.xlsx"
sheet_name_list = ["register", "login", "recharge", "withdraw"]
test_register = read_test_datas(test_table_name, sheet_name_list[0])
test_register_datas = test_register.obtain_datas()
# pprint(test_register_datas)
test_login = read_test_datas(test_table_name, sheet_name_list[1])
test_login_datas = test_login.obtain_datas()
# pprint(test_login_datas)
test_recharge = read_test_datas(test_table_name, sheet_name_list[2])
test_recharge_datas = test_recharge.obtain_datas()
# pprint(test_recharge_datas)
test_withdraw = read_test_datas(test_table_name, sheet_name_list[3])
test_withdraw_datas = test_withdraw.obtain_datas()
# pprint(test_withdraw_datas)

