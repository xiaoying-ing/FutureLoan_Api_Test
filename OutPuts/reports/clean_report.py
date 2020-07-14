# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   clean_report.py

@Time    :   2020/7/14 16:16

@Desc    :

'''
from Common.handle_remove_file import del_files
from Common.handle_path import reports_dir

remove_mark = ".html"
del_files(reports_dir, remove_mark)