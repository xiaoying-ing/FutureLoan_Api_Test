# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_del_EnvData_attr.py

@Time    :   2020/7/22 17:36

@Desc    :

'''
from Common.handle_case_relpace_data import EnvData
import re

all_attr = dir(EnvData)


# print(all_attr)
def del_one_attr(attr_name):
    delattr(EnvData, attr_name)


def clean_EnvData_attr():
    for attr in all_attr:
        if re.findall("__.*?__", attr):
            pass
        else:
            delattr(EnvData, attr)

# clean_attr = clean_EnvData_attr()
# attr = dir(EnvData)
# print(attr)
