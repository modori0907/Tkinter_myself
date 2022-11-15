import glob
import os.path
import re
import tkinter
import tkinter.filedialog
from tkinter import messagebox, IntVar  # Intvarは変数を保持するために利用する

"""
作りたい機能
iniファイル的なものを作成する
"""
# ------- 変数の定義 ------- #
# フォントの定義
basic_font = ('Times New Roman', 15)
list_font = ('Times New Roman', 20)

# products_mem = {"ACM": 100, "AES":200}
products_mem = [100, 200]

# 対象ファイルを入れるフォルダ
mem_source_files = []
cpu_source_files = []


# ------- ウインドウ作成 ------- #
root = tkinter.Tk()
root.title("Analog")

# root.iconbitmap('') # 利用するのであれば
root.geometry('500x600')  # ウインドウのサイズ
root.resizable(0, 0)  # ウインドウサイズの変更。許可しない


# ラジオボタンの変数保持用のインスタンスを作成
# root=tkinter.Tkの下に作成すること。

source_memory = IntVar()
source_memory.set(products_mem[0])  # 初期値の指定

# ------- 関数の作成 ------- #

# ファイル、フォルダ情報の取得
def add_item():
    initial_dir = "./"

    # -- ファイル情報の取得
    # file_type = [("text", "*.txt"), ("Log", "*.log")]  # ファイルの種類を選択
    # file_name = tkinter.filedialog.askopenfilename(file_type=file_type, initialdir="./") # ファイルの選択
    # my_listbox.insert(END, file_name)# 取得した値をリストブックス(ここではtkinter.Listbox)に挿入するやりかた例。 ENDは一番最後の行に追加するオプション

    # -- フォルダ情報およびフォルダ内のファイル情報を取得、加工
    folder_name = tkinter.filedialog.askdirectory(initialdir=initial_dir)  # フォルダ選択
    # フォルダの中身をリスト形式で取得する
    # os.path.joinを使うことで取得したフォルダパスに*を追加する。例￥ss¥sss¥ss(¥*.txt)の二つ目の引数を追加するイメージ
    in_files = glob.glob(os.path.join(folder_name, "*"))

    # 条件に合致したフォルダパスのみをリストに追加する
    global mem_source_files
    global cpu_source_files

    for x in in_files:
        if re.search(r"mem.txt$", x):
            mem_source_files.append(x)
        elif re.search(r"cpu.txt$", x):
            cpu_source_files.append(x)
    # 条件を満たしているか確認。
    numbers_files = (len(cpu_source_files) + len(mem_source_files))

    if numbers_files % 2 == 0:
        list_add_box.insert(tkinter.END, folder_name)
        # 条件に合致したら画面上に文字を表示させる
        list_cpu_number = tkinter.Label(file_frame, text=f"CPUファイル: {len(cpu_source_files)}")
        list_cpu_number.grid(row=1, column=1, pady=15, ipadx=5)
        list_mem_number = tkinter.Label(file_frame, text=f"MEMファイル: {len(mem_source_files)}")
        list_mem_number.grid(row=2, column=1, pady=15, ipadx=5)

    else:
        messagebox.showinfo(f"ファイルの数が{numbers_files}です。/n 再度対象ファイルの数を確認してください")
        mem_source_files = []
        cpu_source_files = []


# フレームの作成
file_frame = tkinter.Frame(root)
file_frame.pack()

choose_mem = tkinter.LabelFrame(root, text="対象プロダクトを選択してください", font=basic_font)
choose_mem.pack(padx=10, pady=10)

# output_frame = tkinter.Frame(root)
# button_frame = tkinter.Frame(root)
# vol_frame = tkinter.Frame(root)
#
# output_frame.pack()
# button_frame.pack()
# vol_frame.pack()







# ------- ボタン ------- #

# オブジェクト作成
list_add_button = tkinter.Button(file_frame, text="フォルダ参照", borderwidth=2, font=basic_font, command=add_item)
list_add_label = tkinter.Label(file_frame, text="PATH", font=basic_font)
list_add_box = tkinter.Entry(file_frame, width=40, font=basic_font)

chose_mem_acm = tkinter.Radiobutton(choose_mem, text=f"ACM: {products_mem[0]} kb", font=basic_font,
                                    variable=source_memory, value=products_mem[0])

chose_mem_acm.grid(row=0, column=0, padx=10, pady=10)

# レジオボタン、対象ラジオをボタンを選んだら、valueで指定した値をvariableで指定した変数に入力する
chose_mem_aes = tkinter.Radiobutton(choose_mem, text=f"AES: {products_mem[1]} kb", font=basic_font,
                                    variable=source_memory, value=products_mem[1])
chose_mem_aes.grid(row=0, column=1, padx=10, pady=10)

# 配置する処理
list_add_label.grid(row=0, column=0, padx=2, pady=15, ipadx=5)  # ipadxは内側の余白
list_add_box.grid(row=0, column=1, padx=2, pady=15, ipadx=5)
list_add_button.grid(row=1, column=0, padx=2, pady=15, ipadx=5)  # ipadxは内側の余白

# list_remove_button = tkinter.Button(file_frame, text="選択、削除", borderwidth=2, font=basic_font)
# list_clear_button = tkinter.Button(file_frame, text="一括削除", borderwidth=2, font=basic_font)
#

# list_remove_button.grid(row=0, column=1, padx=2, pady=15, ipadx=5)
# list_clear_button.grid(row=0, column=2, padx=2, pady=15, ipadx=5)
#
# # スクロールバーの追加
# # 横方向にスクロールバーを変更することもできる orientを追加する
# my_scrollbar = tkinter.Scrollbar(output_frame)
#


# # 音楽リストの作成
# my_listbox = tkinter.Listbox(output_frame, width=45, height=15, yscrollcommand=my_scrollbar.set, borderwidth=3,
#                              font=list_font)
# my_listbox.grid(row=0, column=0)
#
# my_scrollbar.config(command=my_listbox.yview)
# my_scrollbar.grid(row=0, column=1, sticky="NS")  # NSは上と下で引き伸ばせる
#
# # 音楽再生に関する再生ボタン作成
# play_button = tkinter.Button(button_frame, text="再生", borderwidth=2, font=basic_font)
# stop_button = tkinter.Button(button_frame, text="一時停止", borderwidth=2, font=basic_font)
# restart_button = tkinter.Button(button_frame, text="再開", borderwidth=2, font=basic_font)
#
# play_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
# stop_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
# restart_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)
#
# # 音量バーの作成
# # 横方向はhorizontal,0-100を表示させたくないのであれば、showvalueを使う
# # from_=0.0, to=1.0, resolution=0.01 刻みを指定することもできる
# vol_label = tkinter.Label(vol_frame, text="音量")
# vol_scale = tkinter.Scale(vol_frame, orient='horizontal', length=300, from_=0.0, to=1.0, resolution=0.01, showvalue=0)
# vol_scale.set(0.1)  # スケールの初期値を設定する
#
# vol_label.grid(row=0, column=0, padx=10)
# vol_scale.grid(row=0, column=1, padx=10)
#
# # ループ処理の実行
# # ウインドウが消えないように
root.mainloop()
