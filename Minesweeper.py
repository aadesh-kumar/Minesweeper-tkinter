from tkinter import *
from tkinter import messagebox
import random

def create_help_window():
    help_window = Toplevel(m)
    help_window.title('Help')
    l = Label(help_window, text = "This is based on Original Minesweeper\n Press left-click to reveal cell and right-click to mark it.")
    l.grid()

first_click = True
mines = 10
count = 0
rows = 8
cols = 8
mine_grid = []
b = []

m = Tk()
m.title('Minesweeper')

menubar = Menu(m, tearoff = 0)

# filemenu
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = 0)
filemenu.add_command(label = 'About', command = 0)
filemenu.add_command(label = 'Quit', command = m.quit)
menubar.add_cascade(label = 'File', menu = filemenu)

# help menu
menubar.add_command(label = 'Help', command = create_help_window)

for i in range(0, rows):
    mine_grid.append([])
    for j in range(0, cols):
        mine_grid[i].append(0)

# initialize the grid
def Init():
    global count, b, first_click
    count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            b[i][j]['state'] = 'normal'
            b[i][j]['bg'] = 'black'
            b[i][j]['text'] = ''
            mine_grid[i][j] = 0
    first_click = True

# click on button
def Button1(x, y):
    global count, first_click, b
    b[x][y]['bg'] = 'white'
    b[x][y]['state'] = 'disabled'
    count += 1

    if (first_click == True):
        mine = mines
        while mine > 0:
            r_x = random.randrange(0, rows)
            r_y = random.randrange(0, cols)
            if r_x != x and r_y != y and mine_grid[r_x][r_y] == 0:
                mine_grid[r_x][r_y] = 1
                mine -= 1
        first_click = False

    if mine_grid[x][y] == 1:
        for i in range(0, rows):
            for j in range(0, cols):
                if mine_grid[i][j] == 1:
                    b[i][j]['bg'] = 'red'
                    b[i][j]['text'] = '*'
        messagebox.showerror("Message", "You lose")
        Init()
    else:
        neighbour_mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                    if mine_grid[x+i][y+j] == 1:
                        neighbour_mines += 1
        if neighbour_mines > 0:
            b[x][y]['text'] = str(neighbour_mines)
        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x+i >= 0 and x+i < rows and y+j >= 0 and y+j < cols:
                        if b[x+i][y+j]['state'] != 'disabled':
                            Button1(x+i, y+j)
        if count == rows * cols - mines:
            messagebox.showinfo("Message", "You win")
            Init()


# rt click on button
def Button2(evt, x, y):
    if b[x][y]['state'] == 'disabled':
        return
    if b[x][y]['text'] == 'X':
        b[x][y]['text'] = ''
    else:
        b[x][y]['text'] = 'X'
        b[x][y]['fg'] = 'white'


m.config(menu = menubar)

for i in range(0, rows):
    b.append([])
    for j in range(0, cols):
        button = Button(m, height=3, width=5, bg='black', command = lambda x=i, y=j:Button1(x,y), activebackground='white')
        button.bind('<Button-3>', lambda evt, x=i, y=j : Button2(evt, x, y))
        button.grid(row=i, column=j)
        b[i].append(button)

m.mainloop()