# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_file_process.py
@time: 2024/4/18 12:26 
@desc: 

"""
import os
import sys


class FileProcess(object):
    """

    """

    def get_resource_path(self, path):
        """
        打包时图片相对路径经过处理获取exe运行时的临时路径
        :param path:
        :return:
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, path)
        return os.path.join(os.path.abspath("."), path)
