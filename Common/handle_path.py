# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_path.py

@Time    :   2020/7/2 11:03

@Desc    :

'''
import os
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 项目根目录

cases_dir = os.path.join(base_dir, "TestCases")  # 测试用例文件目录
test_datas_dir = os.path.join(base_dir, "TestDatas")  # 测试数据的目录
reports_dir = os.path.join(base_dir, "OutPuts\\reports")  # 测试报告目录
logs_dir = os.path.join(base_dir, "OutPuts\\logs")  # 日志文件目录
conf_dir = os.path.join(base_dir, "Conf")  # 配置文件的目录
local_time = time.strftime('%Y%m%d-%H%M', time.localtime(time.time()))  # 格式化本地时间
