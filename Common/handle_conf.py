"""
-*- coding:utf-8 -*-
@ Time     :  14:05
@ Name     :  handle_ini_file.py
@ Author   :  xiaoyin_ing
@ Email    :  2455899418@qq.com
@ Software :  PyCharm
 ...
 
"""
from configparser import ConfigParser
from Common.handle_path import conf_dir
import os


class HandleConfig(ConfigParser):
    def __init__(self, ini_file_neme):
        super().__init__()
        self.ini_file_neme = ini_file_neme

    def red_conf__(self):
        file_path = os.path.join(conf_dir, self.ini_file_neme)
        self.read(file_path, encoding="utf-8")


red_conf = HandleConfig("xiaoyin.ini")
red_conf.red_conf__()
log_data_list = [red_conf.get("log", "log_name"), red_conf.get("log", "log_level"), red_conf.getboolean("log", "file")]
# print(log_data_list)
