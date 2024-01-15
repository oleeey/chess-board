from tkinter import *

GAME_WIDTH = 600
GAME_HEIGHT = 600
BLOCK_SIZE = GAME_WIDTH / 8

win = Tk()
win.title("Schachbrett")

canvas = Canvas(win, width=GAME_WIDTH, height=GAME_HEIGHT, background="gray", bd=-2)
canvas.pack()

chars = ["a","b","c","d","e","f","g","h"]

for num in range(1, 9):
    for char in chars:
        if num % 2:
            color = "black"
        else:
            color = "white"

        x0 = BLOCK_SIZE * chars.index(char)
        y0 = GAME_HEIGHT - (BLOCK_SIZE * num)
        x1 = BLOCK_SIZE * (chars.index(char) + 1)
        y1 = GAME_HEIGHT - (BLOCK_SIZE	* (num - 1))
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)


win.update()



winWidth = win.winfo_width()
winHeight = win.winfo_height()
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()
x = int((screenWidth/2) - (winWidth/2))
y = int((screenHeight/2) - (winHeight/2))

win.geometry(f"{winWidth}x{winHeight}+{x}+{y}")

win.mainloop()