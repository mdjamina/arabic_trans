from sre_parse import State
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Notebook,Style
from awesometkinter.bidirender import add_bidi_support, render_bidi_text, derender_bidi_text
from trans_tools import transliterate as transFunct

import os


class FrameGui(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        pass

    def addLabel(self, text, padx="15px"):
        tk.Label(self, text=text).pack(padx=padx, fill='x')

    def createLabel(self, text, padx="15px"):
        lb = tk.Label(self, text=text)
        lb.pack(padx=padx, fill='x')
        return lb

    def addButton(self, titre, command, padx="10px", pady="5px"):
        genButton = tk.Button(self)
        genButton["text"] = titre
        genButton["command"] = command
        genButton.pack(padx=padx, pady=pady)

    def createButton(self, titre, command, padx="10px", pady="5px", state='disabled'):
        genButton = tk.Button(self, state=state)
        genButton["text"] = titre
        genButton["command"] = command
        genButton.pack(padx=padx, pady=pady)
        return genButton

    def addTextInput(self, text="", padx="5px", pady="5px"):

        self.textEntry = tk.Entry(self, justify="right", width=50)
        self.textName = tk.StringVar()
        self.textName.set(render_bidi_text(text))
        self.textEntry["textvariable"] = self.textName

        #self.textEntry.place( x=padx, y=pady,width=250, height=250)

        self.textEntry.pack(fill="both", padx=padx, pady=pady)

        add_bidi_support(self.textEntry)

        # Execute event after pressed any key
        self.textEntry.bind('<KeyRelease>', self.onKeyPress)

    def addTextOutput(self, padx="5px", pady="5px"):

        self.textOutput = tk.Text(self, wrap=tk.WORD)
        self.textOutput.pack(fill="both", padx=padx, pady=pady)


class TextTransGui(FrameGui):

    def createWidgets(self):

        self.input_text = ""

        self.font = tkFont.Font(family="Arial", size=12)

        self.addLabel("Texte :")

        self.addTextInput(self.input_text)

        self.addButton("Transliterate", self.onButtonPress)

        self.addTextOutput()

    def onKeyPress(self, event):
        """Callback
        """
        value = event.widget.get()

        #print("value of %s is '%s'" % (event.widget._name, value))

        self.textOutput.delete(1.0, "end")

        output = transFunct(value)

        self.textOutput.insert(tk.INSERT, output)

    def onButtonPress(self):

        self.input_text = self.textName.get()

        #print("self.input_text:", self.input_text)

        self.textOutput.delete(1.0, "end")

        output = transFunct(derender_bidi_text(self.input_text))
        self.textOutput.insert(tk.INSERT, output)


class FileTransGui(FrameGui):

    def createWidgets(self):

        self.font = tkFont.Font(family="Arial", size=12)

        #self.addLabel("Texte :")

        self.addButton("Browse Files", self.browseFiles)

        self.label_file_explorer = self.createLabel("")

        self.trans_btn = self.createButton("Transliterate", self.onButtonPress)

        self.addTextOutput()

    def browseFiles(self):
        """# Function for opening the
        # file explorer window
        # """

        pwd = os.path.dirname(os.path.abspath(__file__))


        pwd = os.path.join(pwd,"..","data")

        print('pwd:',pwd)

        fname = tk.filedialog.askopenfilename(initialdir=pwd,
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.txt*"),
                                                         ("all files",
                                                          "*.*")))
        print(type(fname), fname)
        if fname:
            self.filename = fname
            msg = "File Opened:"
            msg += "\nPath: {0}".format(self.filename)
            file_size = os.path.getsize(self.filename)
            msg += "\nFile Size : {0} bytes".format(file_size)
            # Change label contents
            self.label_file_explorer.configure(text=msg)
            self.trans_btn["state"] = 'active'

    def onButtonPress(self):

        input_text = self.openFile()

        #print("self.input_text:", self.input_text)
        output = transFunct(input_text)

        self.textOutput.delete(1.0, "end")
        
        self.textOutput.insert(tk.INSERT, output)

    def openFile(self, encoding='utf8'):

        with open(self.filename, 'r',encoding=encoding) as f:
            return f.read()


class TransNotbook(Notebook):

    def __init__(self, master=None):

        # Create an instance of ttk style
        #style = Style()
        #style.theme_use('default')
        #style.configure('TNotebook.Tab', background="Red")
        #style.map("TNotebook", background= [("selected", "red"),("selected", "green")])
        
        
        Notebook.__init__(self, master)
        
        tab1 = TextTransGui(self)
        tab2 = FileTransGui(self)
        self.add(tab1, text='Text')
        self.add(tab2, text='File')
        self.pack(fill=tk.BOTH, padx="10px", pady="5px" ,expand=True)
    


