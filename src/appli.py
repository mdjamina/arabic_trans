import tkinter

from gui import TransGui



if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x700")
    root.wm_title("Arabic transliteration")
    app = TransGui(root)
    app.mainloop()
