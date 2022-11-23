# 設定ファイル作成用
import configparser
import tkinter
from configparser import ConfigParser
from tkinter import messagebox

import json

def read_ini(read_ini, major_config, *configs):

    """
    :param read_ini: iniファイルの名前をフルパスで指定
    :param major_config: 大項目の値を指定 [xxxx]
    :param configs: 各大項目の小項目を指定 [xxxx]の下にあるxxxx= xxxxにあたる。リストで指定してください
    :return: コンフィグの値を取得します・
    """

    i = 0 # config.iniの値を取得するため
    try:
        config = configparser.ConfigParser()
        config.read(read_ini)
        for i in range(0, major_config[i]):
            for _i in range(0, len(configs[i])):
                write_config = json.loads(config.get(major_config[i], configs[i][_i]))
                return write_config
    except:
        pass

"""
参照URL
複数iniファイルの引き渡し
https://itips.krsw.biz/python-configparser-ini-read-list/

"""
