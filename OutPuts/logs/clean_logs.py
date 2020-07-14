# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   clean_logs.py

@Time    :   2020/7/14 16:03

@Desc    :

'''
from Common.handle_remove_file import del_files
from Common.handle_path import logs_dir

remove_mark = ".log"
del_files(logs_dir, remove_mark)