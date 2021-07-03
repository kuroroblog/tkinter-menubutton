import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 1. menubuttonを作成する
        # frame Widget(Frame)を親要素として、menubutton Widgetを作成する。
        # text : テキスト情報
        mb = tk.Menubutton(frame, text="Select alphabet")

        # frame Widget(Frame)を親要素とした場合に、menubutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        mb.pack()

        # 2. menuを作成する
        # menubutton Widgetを親要素として、menu Widgetを作成する。
        # Menuについて : https://kuroro.blog/python/ZITZ7dM4nundAhMbChXs/
        menu = tk.Menu(mb)
        # menuへ選択肢を追加する。
        # label : 選択肢のテキスト。'A'とする。
        menu.add_command(label="A")
        # menuへ選択肢を追加する。
        # label : 選択肢のテキスト。'B'とする。
        menu.add_command(label="B")

        # 3. menubutton内へmenuを入れる
        # menubutton Widgetのmenu optionへ、作成したmenuを入れる。
        mb["menu"] = menu

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
