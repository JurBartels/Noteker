import tkinter as tk
import database
import Frames

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create a toplevel menu
        menubar = tk.Menu(self)
        menubar.add_command(label="New call", command=lambda: self.show_frame("QuestionList"))
        menubar.add_command(label="Search", command=lambda: self.show_frame("Search"))

        # display the menu
        self.config(menu=menubar)

        self.frames = {}
        for F in (Frames.QuestionList,Frames.Search):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("QuestionList")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
           
if __name__ == "__main__":
    app = App()
    app.mainloop()
        
