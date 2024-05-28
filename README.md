# PyinstallerTools
Pyinstaller打包Python小工具

![image-20240528162904517](https://collection-data.bj.bcebos.com/jiaohaicheng/selfspace/b16717b4_60ff_4cb1_9a37_639b89c38d37/image-20240528162904517.png?authorization=bce-auth-v1%2F359794b9ccff4c03a01bdaaf0ede3be2%2F2024-05-28T08%3A29%3A22Z%2F-1%2F%2Fd30a728fe91f247b35d6d54cdbdf2df984c1aa94beaf0c28f4cbf1c826ecab8f)

1. 所有带 * 的都必须填入

2. Pyinsatller.exe 路径， 需要选择本地环境中的Pyinstaller.exe绝对路径 

   例如：D:\Project\Python\pythondevelopmenttools\venv\Scripts\pyinstaller.exe

3. ico 路径，填不填都行

4. temp_path 路径： 必须是个空文件夹，用于存放临时文件以及打包结果

5. 项目入口文件：每个项目都必须有一个启动文件，例如本项目的 start.py 文件 

6. 启动动画路径：程序启动前加载的图片，避免白屏，闪屏，必须是.png格式图片

7. 是否开启单文件模式：关闭后打包结果非单文件

8. 是否清理临时文件：关闭后不会清理打包过程中生成的 build/ spec/

9. 是否隐藏命令行窗口：默认隐藏

10. 图片，音视频等资源文件路径：需要手动填入，一些资源文件所在的 目录

11. 二进制文件目录：需要手动填入，一些二进制资源文件所在的 目录

12. 第三方资源包目录：当打包运行后缺失某些包时，把缺失的包所在目录填进去

13. 一些无法导入的系统模块：如打包后出现无法导入 sys,os等模块 把提示无法导入或找不到的模块填进去，若有多个，用逗号分隔

14. EXE名：打包后的exe文件名，默认和程序启动文件同名，支持自定义

14. 附加指令集，可以输入一些pyinstaller支持的其他命令（其中有一些违禁指令禁止输入，避免直接通过指令集打包产生问题）

15. 打包完成后 开始打包按钮会自动变回可点击状态

16. 所有日志会显示在最下边的日志区

13. 尽量不要打包一半强制退出程序

添加资源文件时打包后容易找不到

解决方案：使用/utils/util_file_process.py中的方法转换下路径就可以了


可执行文件(发行版)：去github Actions 里找


**如遇到其他打包问题联系作者：**

**邮箱:JHC000abc@163.com**



