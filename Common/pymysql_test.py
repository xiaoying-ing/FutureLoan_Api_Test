# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   pymysql_test.py

@Time    :   2020/7/6 10:01

@Desc    :

'''
import pymysql
# from pprint import pprint

# 建立连接
conn = pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    database="futureloan",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标
cur = conn.cursor()
# 执行sql语句
sql = 'select * from member where mobile_phone=18770915871'
count = cur.execute(sql)

# 获取执行语句之后的结果
res_one = cur.fetchone()
print("1:", res_one)
# res_two = cur.fetchone()
# print("2:", res_two)
# all = cur.fetchall()
# pprint(all)
cur.close()
conn.close()
