# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: PlaySong.py
@time: 2024/05/31 20:27:03
@desc:

"""
import os.path
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from utils.util_file_process import FileProcess


class PlaySong(object):
    """
    ubutnu下使用要安装插件：
        sudo apt-get install gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
    """

    def __init__(self):
        self.fp = FileProcess()
        # 音频文件夹
        self.folder = self.fp.get_resource_path(R"gui/res/music")
        self.media_player = QMediaPlayer()
        self.media_player.setVolume(100)

    def play_audio(self):
        """

        :return:
        """
        file_path = os.path.join(self.folder, "chinese.mp3")
        media = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media)
        self.media_player.setVolume(100)
        self.media_player.play()
        self.media_player.stateChanged.connect(self.handle_state_changed)

    def handle_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            # 重新播放音频
            self.media_player.setPosition(0)
            self.media_player.play()
