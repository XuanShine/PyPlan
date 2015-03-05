
import tkinter as tk

class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        doodle_input = tk.Text(self, width= 100)
        doodle_input.pack()
        doodle_input.dump("1.0")
        
app = Application()

app.mainloop()
