# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   moudle_logger.py

@Time    :   2020/6/18 9:42

@Desc    :

'''
import logging
from Common.handle_path import logs_dir, local_time
from Common.handle_conf import log_data_list
import os


class CustomizeLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        super().__init__(name, level)
        fmt_customize = '%(asctime)s-%(name)s-%(levelname)s-%(lineno)d line-%(message)s'
        log_fmt = logging.Formatter(fmt_customize)
        handle_con = logging.StreamHandler()
        handle_con.setFormatter(log_fmt)
        handle_con.setLevel(logging.INFO)
        self.addHandler(handle_con)  # 创建控制台日志输出

        if file:
            file_log_name = name + "-" + local_time
            file = file_log_name + ".log"
            file = os.path.join(logs_dir, file)
            handle_file = logging.FileHandler(file, encoding="utf-8")
            handle_file.setFormatter(log_fmt)
            handle_file.setLevel(logging.INFO)
            self.addHandler(handle_file)  # 创建文件输出日志，格式化时间作为日志文件的名字


myLogger = CustomizeLogger(*log_data_list)
if __name__ == '__main__':
    myLogger.info("第一次日志")

