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

        # frame Widget(Frame)を親要素として、menubutton Widgetを作成する。
        # text : テキスト情報
        mb = tk.Menubutton(frame, text="Select alphabet")

        # menubutton Widgetに紐づく、Menuを作成する。
        # Menuについて : https://kuroro.blog/python/ZITZ7dM4nundAhMbChXs/
        menu = tk.Menu(mb)
        # Menu内に選択肢を追加する。
        # label : 選択肢のテキスト。'A'とする。
        menu.add_command(label="A")
        # Menu内に選択肢を追加する。
        # label : 選択肢のテキスト。'B'とする。
        menu.add_command(label="B")

        # menu optionへ作成したMenuを格納する。
        mb["menu"] = menu

        # frame Widget(Frame)を親要素とした場合に、menubutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        mb.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
