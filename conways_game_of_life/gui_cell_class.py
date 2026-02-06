import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.wm_title('Conway\'s Game of Life')

        self._frame = MainFrame(self)

    
    def run(self):
        self.update()
        self._frame.update()
        self.mainloop()
        
        
class MainFrame(ttk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.pack(fill=tk.BOTH,expand=True,ipadx=0, ipady=0)


        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2000)
        self.rowconfigure(0,weight=2000)
        self.rowconfigure(1,weight=1)

        next_button = ttk.Button(self,text='Step')
        next_button.grid(column=0,row=1, sticky=tk.W, padx=5,pady=1)

        clear_button = ttk.Button(self,text='Clear')
        clear_button.grid(column=0,row=1, sticky=tk.W, padx=5,pady=1)


        canvas = GameCanvas(self)
        # canvas.pack(fill=tk.BOTH,expand=True, ipadx=0, ipady=0)
        canvas.grid(column=0,row=0,columnspan=2,sticky='NSEW', padx=5, pady=3)
        
        self._canvas = canvas

    def update(self):
        self._canvas.draw()
        
class GameCanvas(tk.Canvas):
    
    def __init__(self,frame):
        super().__init__(frame,borderwidth=0, highlightthickness=0)
        self._cells = list()

    
    def draw(self):

        cell_size = 37

        cols = self.winfo_width() // cell_size
        rows = self.winfo_height() // cell_size


        margin_x = (self.winfo_width() % cell_size)/2
        margin_y = (self.winfo_height() % cell_size)/2

        
        for row in range(0,rows):
            row_list = list()
            self._cells.append(row_list)

            for col in range(0,cols):
                x = (col * cell_size) + margin_x
                y = (row * cell_size) + margin_y
                id = self.create_rectangle(x,y,x+cell_size,y+cell_size, outline='grey', fill='black')
                row_list.append(Cell(id))
        print(self._cells)

class Cell:
    def __init__(self,id):
        self._id = id
    
    def __str__(self):
        return f'This is the id {id}'

def main():
    app = App()
    app.run()
    

   

main()