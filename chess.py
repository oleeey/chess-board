from tkinter import *
from itertools import cycle

GAME_WIDTH = 600
GAME_HEIGHT = 600
BLOCK_SIZE = GAME_WIDTH / 8

win = Tk()
win.title("Schachbrett")
win.resizable(False, False)

figureImages = {
                "white": {
                    "pawn": PhotoImage(file="img\\white-pawn.png"),
                    "bishop": PhotoImage(file="img\\white-bishop.png"),
                    "rook": PhotoImage(file="img\\white-rook.png"),
                    "knight": PhotoImage(file="img\\white-knight.png"),
                    "king": PhotoImage(file="img\\white-king.png"),
                    "queen": PhotoImage(file="img\\white-queen.png")}, 
                "black": {
                    "pawn": PhotoImage(file="img\\black-pawn.png"),
                    "bishop": PhotoImage(file="img\\black-bishop.png"),
                    "rook": PhotoImage(file="img\\black-rook.png"),
                    "knight": PhotoImage(file="img\\black-knight.png"),
                    "king": PhotoImage(file="img\\black-king.png"),
                    "queen": PhotoImage(file="img\\black-queen.png")}
                }

class Figure():
    def __init__(self, t, t2, c):
        self.type = t
        self.tile = t2
        self.color = c
        self.img = figureImages[self.color][self.type]
        canvas.create_image(canvas.coords(self.tile)[0], canvas.coords(self.tile)[1], image=self.img, anchor=NW)
        
    def getTile(self):
        return self.tile
    
    def getColor(self):
        return self.color
    
    
canvas = Canvas(win, width=GAME_WIDTH, height=GAME_HEIGHT, background="gray", bd=-2)
canvas.pack()

chars = ["a","b","c","d","e","f","g","h"]

color1 = "#769656"
color2 = "#eeeed2"

for num in range(1, 9):
    if num % 2:
        myIterator = cycle([color1, color2])
    else: 
        myIterator = cycle([color2, color1])

    for char in chars:
        color = next(myIterator)

        x0 = BLOCK_SIZE * chars.index(char)
        y0 = GAME_HEIGHT - (BLOCK_SIZE * num)
        x1 = BLOCK_SIZE * (chars.index(char) + 1)
        y1 = GAME_HEIGHT - (BLOCK_SIZE	* (num - 1))
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0, tag=char + str(num))

win.update()

winWidth = win.winfo_width()
winHeight = win.winfo_height()
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()
x = int((screenWidth/2) - (winWidth/2))
y = int((screenHeight/2) - (winHeight/2))

win.geometry(f"{winWidth}x{winHeight}+{x}+{y}")

def drawFigures():
    for i in range(0,8):
        Figure("pawn", chars[i] + str(2), "white")
        Figure("pawn", chars[i] + str(7), "black")

    for c in ["a", "h"]:       
        Figure("rook", c + str(1), "white")
        Figure("rook", c + str(8), "black")

    for c in ["b", "g"]:
        Figure("knight", c + str(1), "white")
        Figure("knight", c + str(8), "black")

    for c in ["c", "f"]:
        Figure("bishop", c + str(1), "white")
        Figure("bishop", c + str(8), "black")

    Figure("queen", "d1", "white")
    Figure("queen", "d8", "black")

    Figure("king", "e1", "white")
    Figure("king", "e8", "black")
    
drawFigures()
        

win.mainloop()