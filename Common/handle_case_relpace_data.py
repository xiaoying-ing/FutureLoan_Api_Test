# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_case_random_data.py

@Time    :   2020/7/7 14:00

@Desc    :

'''
import re
from Common.handle_conf import red_conf


class EnvData:
    """
    存储用例要使用到的数据。
    """
    money = None
    member_id = None
    token = None
    pass


def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)

def replace_case_by_reglur(case):
    '''
    对excel用例中读取出来的整条测试用例做全部替换
    包括 url,request_data,expected,check_sql
    :param case: 一整条完整的测试用例
    :return: 替换后的测试用例
    '''
    for key, value in case.items():
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_by_regular(value)
    return case


def replace_by_regular(data):
    '''
    将字符串当中，匹配#(.*?)#部分，替换对应的真实数据。
    将真实数据只从2个地方去获取：1.配置文件中的data区域；2.EvnData的类属性（全应是字符串类型）
    :param data: 字符串
    :return: 返回替换后的字符串
    '''
    res = re.findall("#(.*?)#", data)
    # print(res)
    # 标识符对应的值，来自于： 1.环境变量 2.配置文件
    if res:
        for item in res:
            try:
                value = red_conf.get("data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    continue
            data = data.replace("#{}#".format(item), value)
    return data


def replace_mark_with_data(case, mark, real_data):
    '''
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    :param case:excel用例中读取的一条数据（一行），是一个字典
    :param mark:数据中的占位符，可被替换的数据
    :param real_data:要被替换的真实数据
    :return:case
    '''
    for key, value in case.items():
        if value is not None and isinstance(value, str):  # 确保数据非空且是一个字符串
            if value.find(mark) != -1:  # 找到占位符
                case[key] = value.replace(mark, real_data)
    return case


if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789"}'
    }

    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "12345555")
        print(case)

    for key, value in case.items():
        print(key, value)
