from tkinter import *
import random

GAME_WIDTH = 700
GAME_HIEGHT = 700
SPEED = 50 
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACK_CLOR = "#000000"


class snake():
    pass
class food():
    pass

def next_turn():
    pass
def change_direction(new_direction):
    pass
def check_colision():
    pass
def game_over():
    pass


window = Tk()
window.title("snake Game")
window.resizable(True,True)

score = 0 
direction = 'down'

Label = Label(window, text = "Score:".format(score), font=('consolas',40))
Label.pack()

Canvas = Canvas(window,bg =BACK_CLOR,height = GAME_HIEGHT,width=GAME_WIDTH)
Canvas.pack()

window.update()

window_width = window.winfo_width()
Window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width/2) - (window_width/2)
y = int(screen_height/2) - (Window_height/2)

# window.geometry(f"{window_width}x{Window_height}+{x}+{y}")

window.mainloop()

