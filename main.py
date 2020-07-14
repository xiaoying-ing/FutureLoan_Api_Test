# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   main.py

@Time    :   2020/7/3 9:55

@Desc    :  生成测试报告

'''
from unittest import TestLoader
from BeautifulReport import BeautifulReport
from Common.handle_path import cases_dir, reports_dir, local_time


test_suit = TestLoader().discover(cases_dir)
br = BeautifulReport(test_suit)
report_module_name = local_time + "-前程贷接口测试"
report_name = local_time + "-前程贷-接口—测试报告.html"
br.report(report_module_name, report_name, reports_dir)

