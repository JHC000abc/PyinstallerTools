# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: ThreadSelf.py
@time: 2024/4/18 10:22 
@desc: 

"""
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


class MyThread(QThread):
    """

    """
    signal_thread_finished = pyqtSignal()

    def __init__(self):
        super(MyThread, self).__init__()

    def add_job(self, func, callback=None, *args, **kwargs):
        """

        :param func:
        :param callback:
        :param args:
        :param kwargs:
        :return:
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.callback = callback

    def run(self):
        """

        :return:
        """
        status = True
        result = ""
        try:
            result = self.func(*self.args, **self.kwargs)
        except:
            status = False
        # 发出任务完成信号
        if self.callback:
            self.callback(status, result)
        self.signal_thread_finished.emit()
