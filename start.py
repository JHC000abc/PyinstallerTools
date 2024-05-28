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
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet
from PyQt5.QtGui import QIcon
from utils.util_file_process import FileProcess

# 禁止闪屏 不打包不生效
try:
    import pyi_splash

    pyi_splash.close()
except ImportError:
    pass


def show_msg_box():
    """

    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(
        "本程序仅是对于Pyinstaller的常用参数进行封装<br>提供可视化界面，简化打包过程<br>请勿将此程序用于打包非法软件，否则后果自负")
    msg_box.setWindowTitle("免责声明")
    msg_box.setWindowIcon(QIcon(FileProcess().get_resource_path(Rf"gui/res/icon/icon.png")))
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.processEvents()
    show_msg_box()
    try:
        apply_stylesheet(app, theme="dark_teal.xml")
    except:
        print("样式加载失败")
    Form = MainUiForm()
    MainUiForm.show(Form)
    sys.exit(app.exec_())
