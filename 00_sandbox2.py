from ipaddress import collapse_addresses
from tkinter import *

def on_enter(e, self, row, col):
    self._btn_matrix[col][row].config(bg="grey", fg="white")

def on_leave(e, self, row, col):
    self._btn_matrix[col][row].config(bg="white", fg="black")

class App(object):
    def __init__(self, master):
        self._master = master

        for col in range(2):
            for row in range(2):
                btn = Button(master, text = '(%d, %d)' % (col, row), bg = 'white')
                btn['command'] = lambda b = btn: b.config(bg = 'black')
                btn.grid(row = row, column = col)

class App(object):
    def __init__(self, master):
        self._master = master
        self._btn_matrix = []

        for col in range(2):
            row_matrix = []
            for row in range(2):
                btn = Button(master, text = '(%d, %d)' % (col, row), bg = 'white',
                                command = lambda x = row, y = col: self.update(x, y))
                btn.grid(row = row, column = col)
                row_matrix.append(btn)
            self._btn_matrix.append(row_matrix)

    def update(self, row, col):
        self._btn_matrix[col][row].bind('<Enter>', lambda e: on_enter(e, self, [row], [col]))
        self._btn_matrix[col][row].bind('<Leave>', lambda e: on_leave(e, self, [row], [col]))

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()