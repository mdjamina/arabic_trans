import tkinter

from gui import TransNotbook



if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("700x550")
    root.wm_title("Transliteration")
    app = TransNotbook(root)
    app.mainloop()
