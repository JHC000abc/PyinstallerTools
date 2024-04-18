# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: start.py
@time: 2024/4/17 14:38 
@desc: 

"""
import sys
from PyQt5 import QtWidgets
from gui.ctrl.ctrl_main import MainUiForm
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.processEvents()
    try:
        apply_stylesheet(app, theme="dark_teal.xml")
    except:
        print("样式加载失败")
    Form = MainUiForm()
    MainUiForm.show(Form)
    sys.exit(app.exec_())
