import tkinter as tk
import database

class QuestionList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.sdescL = tk.Label(self)
        self.sdescL["text"] = "Short description"
        self.sdescL.grid(row = 0, columnspan = 2)

        self.sdescE = tk.Entry(self, width = 35)
        self.sdescE.grid(row = 1, pady = (10,10), columnspan = 2)
        
        self.fnrL = tk.Label(self)
        self.fnrL["text"] = "Filiaalnr"
        self.fnrL.grid(row = 2,columnspan = 2)
        
        self.fnrE = tk.Entry(self)
        self.fnrE.grid(row = 3, pady = (10,10),columnspan = 2)

        self.knrL = tk.Label(self)
        self.knrL["text"] = "Kassa nr"
        self.knrL.grid(row = 4)
        
        self.knrE = tk.Entry(self, width = 15)
        self.knrE.grid(row = 5, pady = (10,10))

        self.kaL = tk.Label(self)
        self.kaL["text"] = "Aantal kassa's"
        self.kaL.grid(row = 4, column = 1)
        
        self.kaE = tk.Entry(self, width = 15)
        self.kaE.grid(row = 5, pady = (10,10), column = 1)

        self.descL = tk.Label(self)
        self.descL["text"] = "Description"
        self.descL.grid(row = 8, columnspan = 2)
        
        self.descT = tk.Text(self, height = 10, width = 30)
        self.descT.grid(row = 9, padx = (10, 10), pady = (20,20) ,columnspan = 2)

        self.b1 = tk.Button(self)
        self.b1.grid(row = 10,columnspan = 2 )
        self.b1["text"] = "Submit"
        self.b1["command"] = self.submit
        
    def submit(self):
        db.insert(self.sdescE.get(), self.fnrE.get(),
                  self.knrE.get(), self.kaE.get(),
                  self.descT.get("1.0","end-1c") )
        db.read()
        print("done submit")

    def clear(self):
        for child in self.winfo_children():
            child.destroy()

class Search(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.searchL = tk.Label(self)
        self.searchL["text"] = "Search"
        self.searchL.grid(row = 0, padx = (10,10))

        self.searchE = tk.Entry(self, width = 15)
        self.searchE.grid(row = 1, pady = (10,10), padx = (10,10))

        self.gobtn = tk.Button(self)
        self.gobtn.grid(row = 2)
        self.gobtn["text"] = "Go"
        self.gobtn["command"] = self.searchOne


    def searchOne(self):
        db.searchOne(self.searchE.get())
    
db = database.Database()
