# !\usr\bin\python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: ctrl_main.py
@time: 2024\4\17 14:36 
@desc: 

"""
import os
import shutil
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from gui.ui.main import Ui_Form
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from utils.util_make_exe import MakeEXE
from manager.ThreadSelf import MyThread


class MainUiForm(QtWidgets.QWidget):

    def __init__(self):
        super(MainUiForm, self).__init__()
        self.make_exe = MakeEXE()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.thread = MyThread()
        self.__view()
        self.__args()
        self.__slot()

    def __view(self):
        """

        :return:
        """
        self.setWindowTitle("Python打包工具")
        self.setFixedSize(755, 890)
        self.ui.lineEdit_pyinstaller.setReadOnly(True)
        self.ui.lineEdit_ico.setReadOnly(True)
        self.ui.lineEdit_temp_path.setReadOnly(True)
        self.ui.lineEdit_file.setReadOnly(True)

    def __args(self):
        """

        :return:
        """
        self.pyinstaller_path = None
        self.ico_path = None
        self.temp_path = None
        self.start_file = None
        self.file_name = None
        self.hidden_import_list = []
        self.splash = None

        # self.pyinstaller_path = R"D:\Project\Python\pythondevelopmenttools\venv\Scripts\pyinstaller.exe"
        # self.ico_path = None
        # self.temp_path = R"C:\Users\v_jiaohaicheng\Downloads\1111"
        # self.start_file = R"D:\Project\Python\pythondevelopmenttools\tests\pyinstaller_test\test.py"

        self.single_file = True
        self.single_clear = True
        self.single_cmd_hide = True

    def __slot(self):
        self.ui.pushButton_pyinstaller.clicked.connect(self.check_pyinstaller)
        self.ui.pushButton_ico.clicked.connect(self.check_ico)
        self.ui.pushButton_temp_path.clicked.connect(self.check_temp_path)
        self.ui.pushButton_file.clicked.connect(self.check_file)
        self.ui.pushButton_start.clicked.connect(self.check_start)
        self.ui.pushButton_splash.clicked.connect(self.check_splash)

        self.ui.checkBox_single.stateChanged.connect(self.check_single_file)
        self.ui.checkBox_clear.stateChanged.connect(self.check_clear)
        self.ui.checkBox_cmd.stateChanged.connect(self.cmd_hide)

        self.make_exe.signal_start.connect(self.start_make_exe)
        self.make_exe.signal_cmd.connect(self.show_cmd_msg)
        self.thread.signal_thread_finished.connect(self.remove_temp_paths)

    def cmd_hide(self):
        """

        :return:
        """
        if self.single_cmd_hide:
            self.single_cmd_hide = False
        else:
            self.single_cmd_hide = True

    def remove_temp_paths(self):
        """

        :return:
        """
        if self.single_clear:
            try:
                shutil.rmtree(os.path.join(os.path.join(self.temp_path, "dist"), "build"))
                shutil.rmtree(os.path.join(os.path.join(self.temp_path, "dist"), "spec"))
                self.make_exe.signal_cmd.emit("临时文件清理完成")
            except:
                self.make_exe.signal_cmd.emit("临时文件清理失败")

    def check_clear(self):
        """

        :return:
        """
        if self.single_clear:
            self.single_clear = False
        else:
            self.single_clear = True

    def check_single_file(self):
        """

        :return:
        """
        if self.single_file:
            self.single_file = False
        else:
            self.single_file = True

    def get_data_list_from_line_edit(self, text):
        """

        :param text:
        :return:
        """
        lis = []
        if text:
            for line in text.split("\n"):
                if os.path.isabs(line) and os.path.isdir(line):
                    lis.append(os.path.abspath(line))
        if lis:
            lis = list(set(lis))
        return lis

    def select_path_file(self, mode=0):
        """

        :return:
        """
        if mode == 0:
            return QFileDialog().getExistingDirectory(self, "请选择文件夹路径", None)
        else:
            return QFileDialog().getOpenFileName(self, "请选择文件路径", None)

    def start_make_exe(self):
        """

        :return:
        """

        def start():
            self.make_exe.process(pyinstaller_path=self.pyinstaller_path, mode="F" if self.single_file else "",
                                  ico=self.ico_path if self.ico_path else "", temp_path=self.temp_path,
                                  third_paths=self.third_paths,
                                  file=self.start_file, data_paths=self.data_paths, binary_paths=self.binary_paths,
                                  single_cmd_hide=self.single_cmd_hide, exe_name=self.file_name,
                                  hiddens=self.hidden_import_list, splash=self.splash)

        self.make_exe.signal_cmd.emit("开始打包")
        self.data_paths = self.get_data_list_from_line_edit(self.ui.textEdit_data_paths.toPlainText())
        self.binary_paths = self.get_data_list_from_line_edit(self.ui.textEdit_binary_paths.toPlainText())
        self.third_paths = self.get_data_list_from_line_edit(self.ui.textEdit_third_paths.toPlainText())
        hidden_import = self.ui.lineEdit_hidden_import.text()
        if hidden_import:
            self.hidden_import_list = hidden_import.split(",")

        self.thread.add_job(start)
        self.thread.start()

    def check_start(self):
        """

        :return:
        """
        if not self.pyinstaller_path:
            self.show_msg("请选择【pyinstaller】路径")
            return
        if not self.temp_path:
            self.show_msg("请选择【临时文件】路径")
            return
        if not self.start_file:
            self.show_msg("请选择【项目启动文件】路径")
            return
        else:
            self.file_name = self.ui.lineEdit_name.text()

        self.make_exe.signal_start.emit()

    def check_splash(self):
        """

        """
        path = self.select_path_file(1)[0]
        if path:
            if path.endswith(".png"):
                self.splash = path
                self.make_exe.signal_cmd.emit(f"选中 【项目启动文件】 路径:{path}")
                self.ui.lineEdit_splash.setText(self.splash)
            else:
                self.show_msg("请选择正确的 项目启动文件 路径\n必须为空文件夹")
        else:
            self.show_msg("请选择正确的 项目启动文件 路径\n必须为空文件夹")

    def check_file(self):
        """

        :return:
        """
        path = self.select_path_file(1)[0]
        if path:
            if path.endswith(".py"):
                self.start_file = path
                self.ui.lineEdit_file.setText(path)
                self.make_exe.signal_cmd.emit(f"选中 【项目启动文件】 路径:{path}")
                self.file_name = os.path.split(self.start_file)[-1].split(".")[0]
                self.ui.lineEdit_name.setText(self.file_name)
            else:
                self.show_msg("请选择正确的 项目启动文件 路径\n必须为空文件夹")
        else:
            self.show_msg("请选择正确的 项目启动文件 路径\n必须为空文件夹")

    def check_temp_path(self):
        """

        :return:
        """
        path = self.select_path_file()
        if path:
            if not os.listdir(path):
                self.temp_path = path
                self.ui.lineEdit_temp_path.setText(path)
                self.make_exe.signal_cmd.emit(f"选中 【临时文件】 路径:{path}")
            else:
                self.show_msg("请选择正确的 临时文件 路径\n必须为空文件夹")
        else:
            self.show_msg("请选择正确的 临时文件 路径\n必须为空文件夹")

    def check_ico(self):
        """

        :return:
        """
        path = self.select_path_file(1)[0]
        if path:
            if path.lower().endswith(".ico"):
                self.ico_path = path
                self.ui.lineEdit_ico.setText(path)
                self.make_exe.signal_cmd.emit(f"选中 【.ico】 路径:{path}")
            else:
                self.show_msg("请选择正确的 .ico 路径")
        else:
            self.show_msg("请选择正确的 .ico路径")

    def show_cmd_msg(self, msg):
        """

        :param msg:
        :return:
        """
        self.ui.textEdit_log.append(f"{msg}")
        if msg == "开始打包":
            self.ui.pushButton_start.setEnabled(False)
        elif msg == "打包完成":
            self.ui.pushButton_start.setEnabled(True)

    def check_pyinstaller(self):
        """

        :return:
        """
        path = self.select_path_file(1)[0]
        if path:
            if path.lower().endswith("pyinstaller.exe"):
                self.pyinstaller_path = path
                self.ui.lineEdit_pyinstaller.setText(path)
                self.make_exe.signal_cmd.emit(f"选中 【Pyinstaller.exe】 路径:{path}")
            else:
                self.show_msg("请选择正确的 Pyinstaller.exe 路径")
        else:
            self.show_msg("请选择正确的 Pyinstaller.exe 路径")

    def show_msg(self, msg):
        """

        :param msg:
        :return:
        """
        msg_box = QMessageBox(QMessageBox.Warning, 'Warning', msg)
        msg_box.setWindowFlags(Qt.FramelessWindowHint)
        msg_box.show()
        msg_box.exec_()

    def closeEvent(self, event):
        """
        关闭窗口触发以下事件
        :return:
        """
        msg = QMessageBox()
        a = msg.warning(self, "退出警告", '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No)
        if a == QMessageBox.Yes:
            self.thread.terminate()
            del self.thread
            os._exit(0)
        else:
            event.ignore()
