from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import configparser, os, webbrowser


class TextEdit:
    _textFilename = ''

    @property
    def textFilename(self):
        return self._textFilename

    @textFilename.setter
    def textFilename(self, value):
        self._textFilename = value
        if value == '':
            root.title(self.__class__.__name__)
            self.menuFile.entryconfigure(
                '保存(S)', state=DISABLED)
        else:
            s = os.path.basename(value)
            if self.isSjis:
                s += ' (SJIS)'
            else:
                s += ' (UTF-8)'
            root.title(s)
            self.menuFile.entryconfigure(
                '保存(S)', state=NORMAL)
            self.directory = os.path.dirname(value)

    def __init__(self, root):
        self.text = ScrolledText(root)
        self.text.pack(expand=1, fill=BOTH)

        self.fileTypes = [
            ('テキストファイル', '*.txt'),
            ('すべてのファイル', '*.*')]
        self.directory = os.getenv('HOMEDRIVE') \
                         + os.getenv('HOMEPATH') + '\\Documents'

        clientHeight = '50'
        clientWidth = '300'
        cp = configparser.ConfigParser()
        try:
            cp.read(self.__class__.__name__ + '.ini')
            clientHeight = cp['Client']['Height']
            clientWidth = cp['Client']['Width']
            self.directory = cp['File']['Directory']
        except:
            print(self.__class__.__name__ +
                  ':Use default value(s)', file=sys.stderr)
        root.geometry(clientWidth + 'x' + clientHeight)
        root.protocol('WM_DELETE_WINDOW',
                      self.menuFileExit)

        root.option_add('*tearOff', FALSE)
        menu = Menu(root)
        self.menuFile = Menu(menu)
        menu.add_cascade(menu=self.menuFile,
                         label='ファイル(F)', underline=5)
        self.menuFile.add_command(label='新規(N)',
                                  underline=3, command=self.menuFileNew)
        self.menuFile.add_command(label='開く(O)',
                                  underline=3, command=self.menuFileOpen)
        self.menuFile.add_command(label='保存(S)',
                                  underline=3, command=self.menuFileSave)
        self.menuFile.add_command(
            label='名前を付けてシフトJISで保存(A)',
            underline=16, command=self.menuFileSaveAsSjis)
        self.menuFile.add_command(
            label='名前を付けてUTF-8で保存(U)',
            underline=15, command=self.menuFileSaveAsUtf8)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='終了(X)',
                                  underline=3, command=self.menuFileExit)

        menuHelp = Menu(menu)
        menu.add_cascade(menu=menuHelp,
                         label='ヘルプ(H)', underline=4)
        menuHelp.add_command(label='Webサイトを開く(W)',
                             underline=10, command=self.menuHelpOpenWeb)
        menuHelp.add_separator()
        menuHelp.add_command(label='バージョン情報(V)',
                             underline=8, command=self.menuHelpVersion)
        root['menu'] = menu

        self.menuFileNew()

    def menuFileNew(self):
        self.isSjis = TRUE
        self.textFilename = ''
        self.text.delete('1.0', 'end')

    def menuFileOpen(self):
        filename = filedialog.askopenfilename(
            filetypes=self.fileTypes,
            initialdir=self.directory)
        if not filename:
            return

        newText = ''
        try:
            f = open(filename, 'r')
            newText = f.read()
            self.isSjis = TRUE
        except:
            f = open(filename, 'r', encoding='UTF-8')
            newText = f.read()
            self.isSjis = FALSE
        finally:
            f.close()

        if newText == '':
            messagebox.showwarning(
                self.__class__.__name__,
                'ファイルを開けませんでした')
        else:
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', newText)
            self.textFilename = filename

    def menuFileSave(self):
        self.fileSave(self.textFilename, self.isSjis)

    def fileSave(self, saveFilename, saveIsSjis):
        s = self.text.get('1.0', 'end')
        if len(s) == 1:
            messagebox.showwarning(
                self.__class__.__name__,
                '保存するテキストがありません')
            return

        if saveIsSjis == TRUE:
            f = open(saveFilename, 'w')
        else:
            f = open(saveFilename, 'w', encoding='UTF-8')
        f.write(s[:-1])
        f.close()
        self.isSjis = saveIsSjis
        self.textFilename = saveFilename

    def menuFileSaveAsSjis(self):
        self.fileSaveAs(TRUE)

    def menuFileSaveAsUtf8(self):
        self.fileSaveAs(FALSE)

    def fileSaveAs(self, saveIsSjis):
        filename = filedialog.asksaveasfilename(
            filetypes=self.fileTypes,
            initialdir=self.directory,
            initialfile=os.path.basename(
                self.textFilename))
        if not filename:
            return
        self.fileSave(filename, saveIsSjis)

    def menuFileExit(self):
        cp = configparser.ConfigParser()
        cp['Client'] = {
            'Height': str(root.winfo_height()),
            'Width': str(root.winfo_width())}
        cp['File'] = {'Directory': self.directory}
        with open(self.__class__.__name__ +
                  '.ini', 'w') as f:
            cp.write(f)
        root.destroy()

    def menuHelpOpenWeb(self):
        webbrowser.open(
            'https://info.nikkeibp.co.jp/media/NSW/')

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += ' Version 0.01(2021/03/10)\n'
        s += '©2021 Hideo Harada\n'
        s += 'with Python ' + sys.version
        messagebox.showinfo(
            self.__class__.__name__, s)


root = Tk()
TextEdit(root)
root.mainloop()
