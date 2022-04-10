import tkinter as tk
import tkinter.font as tkFont
from awesometkinter.bidirender import add_bidi_support, render_bidi_text, derender_bidi_text
from trans_tools import arabic


class TransGui(tk.Frame):

    def __init__(self, master=None):
        self.input_text = u'السلام عليكم'

        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.font = tkFont.Font(family="Arial", size=12)

        self.addLabel("Texte :")

        self.addTextInput()

        self.addButton("Transliterate", self.onButtonPress)

        self.addTextOutput()

    def addLabel(self, text, padx="15px"):
        tk.Label(self, text=text).pack(padx=padx, fill='x')

    def addButton(self, titre, command, padx="10px", pady="5px"):
        self.genButton = tk.Button(self)
        self.genButton["text"] = titre
        self.genButton["command"] = command
        self.genButton.pack(padx=padx, pady=pady)

    def addTextInput(self, text="", height=115, padx="5px", pady="5px"):

        self.textEntry = tk.Entry(self, justify="right", width=50)
        self.textName = tk.StringVar()
        self.textName.set(render_bidi_text(text))
        self.textEntry["textvariable"] = self.textName

        #self.textEntry.place( x=padx, y=pady,width=250, height=250)

        self.textEntry.pack(fill="both", padx=padx, pady=pady)

        add_bidi_support(self.textEntry)


        #Execute event after pressed any key
        self.textEntry.bind('<KeyRelease>',self.onKeyPress)

    def addTextOutput(self, height=115, padx="5px", pady="5px"):

        self.textOutput = tk.Text(self, wrap=tk.WORD)
        self.textOutput.pack(fill="both", padx=padx, pady=pady)

        #scrollbar = tk.Scrollbar(self.textInput, command=self.textInput.yview)

        # self.textInput.config(yscroll=scrollbar.set)

        #self.textInput.pack( fill="both",padx=padx, pady=pady)
        # ['yscrollcommand'] = scrollbar.set

        # self.textInput.configure(font=self.font)

        # scrollbar.pack(fill=tk.Y,side="left")

    def onKeyPress(self,event):
        """Callback
        """        
        value = event.widget.get()        
        
        #print("value of %s is '%s'" % (event.widget._name, value))
        
        self.textOutput.delete(1.0, "end")

        output = self.transliterate(value)
        
        self.textOutput.insert(tk.INSERT, output)

    def onButtonPress(self):

        self.input_text = self.textName.get()

        #print("self.input_text:", self.input_text)

        self.textOutput.delete(1.0, "end")

        output = self.transliterate(derender_bidi_text(self.input_text))
        self.textOutput.insert(tk.INSERT, output)

    def transliterate(self,text):

        #detect language
        #TODO

        lang = 'ara'

        if lang == 'ara':
            return arabic.transliterate(text)

        return ""




if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x700")
    root.wm_title("Arabic transliteration")
    app = TransGui(root)
    app.mainloop()
