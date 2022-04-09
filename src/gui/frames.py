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

        self.addTextInput(self.input_text)

        self.addButton("Transliterate",self.generate)



        self.textOutput = tk.Text(self)
        self.textOutput.pack(fill="both", padx="5px", pady="5px")
        self.textOutput.tag_config("hacker", foreground="green")
        self.textOutput.tag_config("warning", foreground="red")

    def addLabel(self, text,padx="15px"):
        tk.Label(self, text=text).pack(padx=padx, fill='x')     

    def addButton(self, titre,command, padx="10px", pady="5px"):
        self.genButton = tk.Button(self)
        self.genButton["text"] = titre
        self.genButton["command"] = command
        self.genButton.pack(padx=padx, pady=pady)

    def addTextInput(self,text, height=115, padx="5px", pady="5px"):                

        self.textInput = tk.Text(self,height=height,width=75,wrap=tk.WORD)

        scrollbar = tk.Scrollbar(self.textInput, command=self.textInput.yview)

        self.textInput.config(yscroll=scrollbar.set)

        self.textInput.pack( fill="both",padx=padx, pady=pady)
        #['yscrollcommand'] = scrollbar.set

        #self.textInput.configure(font=self.font)

        scrollbar.pack(fill=tk.Y,side="left")

        

        self.textInput.tag_configure('tag-right', justify='right',rmargin=5)

        self.textInput.delete('1.0','end')               

        self.textInput.insert(tk.INSERT,render_bidi_text(text),'tag-right')


        
        
        add_bidi_support(self.textInput)

 
    def generate(self):

        self.input_text = self.textInput.get('1.0','end')

        print("self.input_text:", self.input_text)

        self.textOutput.delete(1.0, "end")

        output = arabic.transliterate(derender_bidi_text(self.input_text))
        self.textOutput.insert("end", output, "hacker")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x700")
    root.wm_title("Arabic transliteration")
    app = TransGui(root)
    app.mainloop()
