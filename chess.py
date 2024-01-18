from tkinter import *
from itertools import cycle

GAME_WIDTH = 600
GAME_HEIGHT = 600
BLOCK_SIZE = GAME_WIDTH / 8

win = Tk()
win.title("Schachbrett")
win.resizable(False, False)

class Figure():
    def __init__(self):
       pass

    def drawImg(self, t, c, img):      
        canvas.create_image(canvas.coords(t)[0], canvas.coords(t)[1], image=img, anchor=NW)
        

    def getTile(self):
        return self.tile
    
    def getColor(self):
        return self.color
    


class Pawn(Figure):
    whitePawn = PhotoImage(file="img\\white-pawn.png")
    blackPawn = PhotoImage(file="img\\black-pawn.png")

    
    def __init__(self, t, c):
        self.tile = t
        self.color = c
        self.image = ""
        super().drawImg(self.tile, self.color, self.image)
        
    
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
    for i in range(1,9):
        Pawn(f'b{i}', "white")


drawFigures()

win.mainloop()