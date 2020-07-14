# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_mysql.py

@Time    :   2020/7/6 10:00

@Desc    :

'''
import pymysql
from Common.handle_conf import red_conf


class HandleDB:
    def __init__(self):
        # 建立连接
        self.connect = pymysql.connect(
            host=red_conf.get("mysql", "host"),
            port=red_conf.getint("mysql", "port"),
            user=red_conf.get("mysql", "user"),
            password=red_conf.get("mysql", "password"),
            database=red_conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建游标
        self.cursor = self.connect.cursor()

    def select_one_data(self, sql):
        self.connect.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def select_all_data(self, sql):
        # self.connect.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_count(self, sql):
        self.connect.commit()
        return self.cursor.execute(sql)

    def update(self, sql):
        """
        对数据库进行增、删、改的操作。
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    TDB = HandleDB()
    TDB.select_one_data('select * from member where mobile_phone="18770915871"')
