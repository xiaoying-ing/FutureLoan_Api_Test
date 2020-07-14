# -*- coding:utf-8 -*-

'''
@Author  :   xiaoyin_ing

@Email   :   2455899418@qq.com

@Software:   PyCharm

@File    :   handle_remove_file.py

@Time    :   2020/7/14 16:06

@Desc    :

'''
import os
from Common.handle_path import logs_dir


def del_files(file_path, start_mark):
    for root, dirs, files in os.walk(file_path):
        for name in files:
            if name.endswith(start_mark):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))


if __name__ == '__main__':
    path = logs_dir
    print(path)
    del_files(path, ".logs")
