# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: Signal.py
@time: 2024/4/17 18:36 
@desc: 

"""

from PyQt5.QtCore import QObject, pyqtSignal


class Signal(QObject):
    signal_start = pyqtSignal()
    signal_cmd = pyqtSignal(str)

