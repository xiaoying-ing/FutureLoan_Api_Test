# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_phone.py

@Time    :   2020/7/6 15:49

@Desc    :

'''
prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199,
          130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 166,
          134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198
          ]

import random
from Common.handle_mysql import HandleDB


def get_new_phone():
    db = HandleDB()
    while True:
        # 1生成
        phone = __generator_phone()
        # 2校验，有
        count = db.get_count('select * from member where mobile_phone="{}"'.format(phone))
        if count == 0:  # 如果手机号码没有在数据库查到。表示是未注册的号码。
            db.close()
            return phone


def get_old_phone():
    '''
    从配置文件获取指定的用户名和密码
    确保此帐号，在系统当中是注册了的。
    返回：用户名和密码。
    :return:
    '''
    from Common.handle_conf import red_conf
    from Common.handle_requests import set_request
    user = red_conf.get("general_user", "user")
    password = red_conf.get("general_user", "password")
    # 如果数据库查找到user，就直接返回。如果没有，则调用注册接口注册一个。
    # 不管注册与否，直接调用注册接口。
    set_request("member/register", "post", {"mobile_phone": user, "pwd": password})
    return user, password


def __generator_phone():
    index = random.randint(0, len(prefix) - 1)
    phone = str(prefix[index])  # 前3位随机prefix里的成员
    for _ in range(0, 8):  # 生成后8位随机数字
        phone += str(random.randint(0, 9))
    return phone


if __name__ == '__main__':
    from Common.handle_requests import set_request
    from pprint import pprint
    user, pwd = get_old_phone()
    pprint([user, pwd])
    response_login = set_request("member/login", "post", {"mobile_phone": user, "pwd": pwd})
    pprint(response_login.json())
