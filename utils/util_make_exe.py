# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: tools.py
@time: 2024/4/17 10:53
@desc:

"""
import os
import subprocess
from manager.Signal import Signal
from PyQt5.QtCore import QObject


class MakeEXE(Signal, QObject):
    """

    """

    def __init__(self):
        super(MakeEXE, self).__init__()

    def check_options_error(self, name, msg):
        """

        :param name:
        :param msg:
        :return:
        """
        if not name:
            raise ValueError(msg)

    def check_options(self, name, default):
        """

        :param name:
        :param msg:
        :return:
        """
        if not name:
            name = default
        return name

    def run_cmd(self, cmd, encoding="utf-8"):
        """

        :param cmd:
        :param encoding:
        :return:
        """
        self.signal_cmd.emit(cmd)
        p = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding=encoding
        )
        while p.poll() is None:
            out = p.stdout.readline().strip()
            if out:
                self.signal_cmd.emit(str(out))

        self.signal_cmd.emit("打包完成")

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        print(kwargs)
        base_cmd = ""
        # Pyinstaller.exe
        pyinstaller_path = kwargs.get("pyinstaller_path")
        self.check_options_error(pyinstaller_path, "请输入pyinstaller.exe路径")

        base_cmd += f"{pyinstaller_path} --clean --noconfirm -y "

        # 单文件
        mode = kwargs.get("mode")
        if mode:
            mode = "-F"
            base_cmd += f"{mode} "

        # 隐藏 cmd 界面
        cmd_hide = kwargs.get("single_cmd_hide")
        if cmd_hide:
            base_cmd += f"-w "

        # 图标
        ico = kwargs.get("ico")
        if ico:
            base_cmd += f"-i {ico} "

        # 临时文件存放位置
        temp_path = kwargs.get("temp_path")
        if temp_path:
            temp_path = os.path.join(temp_path, "dist")
            base_cmd += f"--workpath={os.path.join(temp_path, 'build')} "
            base_cmd += f"--specpath={os.path.join(temp_path, 'spec')} "
            base_cmd += f"--distpath={temp_path} "

        # 图片，音视频文件路径
        data_paths = kwargs.get("data_paths")
        if data_paths:
            for path in data_paths:
                path_last_folder = os.path.split(path)[-1]
                base_cmd += f"--add-data={path}:{path_last_folder} "

        # 二进制文件路径
        binary_paths = kwargs.get("binary_paths")
        if binary_paths:
            for path in binary_paths:
                path_last_folder = os.path.split(path)[-1]
                base_cmd += f"--add-binary={path}:{path_last_folder} "

        # pyinstaller无法自动识别的缺失环境路径
        third_paths = kwargs.get("third_paths")
        if third_paths:
            flag = False
            base_cmd += "--paths="
            for path in third_paths:
                if not flag:
                    if len(third_paths) > 1:
                        base_cmd += f"{path};"
                    else:
                        base_cmd += f"{path}"
                    flag = True
                else:
                    base_cmd += f"{path}"
            base_cmd += " "

        hiddens = kwargs.get("hiddens")
        if hiddens:
            for path in hiddens:
                base_cmd += f'--hidden-import "{path}" '

        splash = kwargs.get("splash")
        if splash:
            base_cmd += f"--splash {splash} "

        exe_name = kwargs.get("exe_name")
        if exe_name:
            base_cmd += f"-n {exe_name} "

        # 项目启动文件路径
        file = kwargs.get("file")
        self.check_options_error(file, "请输入要打包的 .py 入口文件路径")
        base_cmd += f"{file}"

        # print("base_cmd", base_cmd)
        os.chdir(os.sep.join(os.path.split(file)[:-1]))
        self.run_cmd(base_cmd)


if __name__ == '__main__':
    me = MakeEXE()
    pyinstaller_path = R"D:\Project\Python\pythondevelopmenttools\venv\Scripts\pyinstaller.exe"
    mode = "F"
    ico = R""
    temp_path = R"D:\Project\Python\pythondevelopmenttools\tests\pyinstaller_test"
    third_paths = []
    file = R"D:\Project\Python\pythondevelopmenttools\tests\pyinstaller_test\test.py"
    data_paths = [R"D:\Project\Python\pythondevelopmenttools\tests\pyinstaller_test\images",
                  R"D:\Project\Python\pythondevelopmenttools\tests\pyinstaller_test\images2"]
    binary_paths = []
    me.process(pyinstaller_path=pyinstaller_path, mode=mode, ico=ico, temp_path=temp_path, third_paths=third_paths,
               file=file, data_paths=data_paths, binary_paths=binary_paths)
