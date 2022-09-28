
import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator") 

        #Creates a button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #Places button using tkinter grid()
        self.btn.grid(padx=(10,10), pady=(10,10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(row=3, column=2, padx=(10,10), pady=(10,10))
        
        label = tk.Label(text="Custom Text Entry")
        label.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        self.entry = tk.Entry()
        self.entry.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        htmlText2 = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent2 = "<html>\n<body>" + htmlText2 + "</body>\n</html>"
        htmlFile.write(htmlContent2)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
        
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
