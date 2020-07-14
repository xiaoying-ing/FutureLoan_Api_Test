# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_case_random_data.py

@Time    :   2020/7/7 14:00

@Desc    :

'''


class EnvData:
    """
    存储用例要使用到的数据。
    """
    member_id = None
    token = None
    pass


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
