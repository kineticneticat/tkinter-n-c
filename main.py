from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, padding=(10))
frame.grid()

squares = [
    ['--','--','--'],
    ['--','--','--'],
    ['--','--','--']
]

buttons = []
turn = 'x'
turns = 0

class _button:
    def __init__(self, x, y, text, loc):
        self.x = x
        self.y = y
        self.text = StringVar()
        self.loc = loc
    def create(self):
        self.text.set(squares[self.x][self.y])
        ttk.Button(frame, textvariable=self.text, command=lambda:buttons[self.loc].press()).grid(row=self.x+1, column=self.y)
    def update_text(self, text):
        squares[self.x][self.y] = text
        self.text.set(text)
    def test(self):
        return [self.x, self.y, self.text, self.loc]
    def press(self):
        global turn, turns, titletext
        if turns == 9 or squares[self.x][self.y] != '--':
            return None
        if turn == 'x':
            self.update_text('x')
            turn = 'o'
        elif turn == 'o':
            self.update_text('o')
            turn = 'x'
        if (squares[0][0] == 'x' and squares[0][1] == 'x' and squares[0][2] == 'x') or (squares[1][0] == 'x' and squares[1][1] == 'x' and squares[1][2] == 'x') or (squares[2][0] == 'x' and squares[2][1] == 'x' and squares[2][2] == 'x') or (squares[0][0] == 'x' and squares[1][0] == 'x' and squares[2][0] == 'x') or (squares[0][1] == 'x' and squares[1][1] == 'x' and squares[2][1] == 'x') or (squares[0][2] == 'x' and squares[1][2] == 'x' and squares[2][2] == 'x') or (squares[0][0] == 'x' and squares[1][1] == 'x' and squares[2][2] == 'x') or (squares[2][0] == 'x' and squares[1][1] == 'x' and squares[0][2] == 'x'):
          print('x wins')
          titletext.set('\nx Wins\n')
        elif (squares[0][0] == 'o' and squares[0][1] == 'o' and squares[0][2] == 'o') or (squares[1][0] == 'o' and squares[1][1] == 'o' and squares[1][2] == 'o') or (squares[2][0] == 'o' and squares[2][1] == 'o' and squares[2][2] == 'o') or (squares[0][0] == 'o' and squares[1][0] == 'o' and squares[2][0] == 'o') or (squares[0][1] == 'o' and squares[1][1] == 'o' and squares[2][1] == 'o') or (squares[0][2] == 'o' and squares[1][2] == 'o' and squares[2][2] == 'o') or (squares[0][0] == 'o' and squares[1][1] == 'o' and squares[2][2] == 'o') or (squares[2][0] == 'o' and squares[1][1] == 'o' and squares[0][2] == 'o'):
          print('o wins')
          titletext.set('\no Wins\n')
        turns += 1
        if turns == 9:
            print('Draw')
            titletext.set('Draw')
titletext = StringVar()
titletext.set('Noughts\nand\nCrosses')


ttk.Label(frame, textvariable=titletext).grid(column=1, row=0)


i=0
for x in range(3):
    for y in range(3):
        buttons.append(_button(x, y, squares[x][y], i))
        buttons[i].create()
        i+=1




root.mainloop()