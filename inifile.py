# 設定ファイル作成用
import configparser
import tkinter
from configparser import ConfigParser
from tkinter import messagebox





# iniファイルの値をリストで取得するために利用
import json

#
test_get = []

"""
iniファイルを反映させる処理"""


try:
    cp = configparser.ConfigParser()
    cp.read("sample.ini")
    test_get = json.loads(cp.get("settings_list", 'SETTINGS_03'))

    print(type(test_get))
    print(test_get)
except:
    print("aa")
    pass


# リストでゲットする方法
# 失敗した時は対象の設定がわかるようにする



# ウィンドウの作成
root = tkinter.Tk()
root.title = ("Menu practice")
root.geometry("240x200")
root.resizable(0, 0)

# --- 関数



# ------- 設定ファイルを変数に入れることができるかチェック -------#


# 関数の定義
# サブ画面を表示させる処理
# def open_setting():
# # ウインドウを開く処理
# subwindow = tkinter.Toplevel()
# subwindow.title("設定")
# subwindow.geometry("200x100+500+150")
#
# subwindow_label = tkinter.Label(subwindow, text="設定画面です")
# subwindow_label.pack(pady=30)


def menuHelpVersion():
    s = "CALDO\n"
    s += "Version 1.0.0\n"
    s += "@2022/11/16 Modori4\n"
    messagebox.showinfo("バージョン情報", s)


def menuFileExit():
    cp = configparser.ConfigParser()
    cp["Client"] = {
        "test_get": "test",
    }
    with open("test.ini", "w") as f:
        cp.write(f)
    messagebox.showinfo('test', str(root.winfo_width()))
    root.destroy()


# メニューバーの作成
# メニューバーの親となるコンテナの作成
menubar = tkinter.Menu(root)
root.config(menu=menubar)

# 設定メニューの作成
setting_menu = tkinter.Menu(menubar, tearoff=0)  # tearoff=0でメニューに線を表示させない
menubar.add_cascade(label="設定", menu=setting_menu)

# ファイルメニューの作成
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="ファイル", menu=file_menu)

# ヘルプ(H)メニューの作成
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="ヘルプ(H)", menu=help_menu)

# 設定メニューにプルダウンメニューを追加
setting_menu.add_command(label="環境設定")  # commandで実行する関数を支持する
setting_menu.add_command(label="終了(E)", command=menuFileExit)

# ファイルメニューにプルダンメニューを追加
file_menu.add_command(label="新規ファイル")

# ヘルプ(H)メニューのプルダウンメニュー
help_menu.add_command(label="バージョン情報(V)", command=menuHelpVersion)

# 条件に合致したら画面上に文字を表示させる

list_cpu_number = tkinter.Label(text=f"{test_get}")
list_cpu_number.grid(row=1, column=1, pady=15, ipadx=5)

root.mainloop()
