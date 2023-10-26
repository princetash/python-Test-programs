import tkinter
import random

game_Over = False
score = 0
Squares_to_clear = 0

def play_bombdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


bombfield = []
def create_bombfield(bombfield):
    global Squares_to_clear
    
    for row in range(0,10):
        row_list = []
        for column in range(0,10):
            if random.randint(1,100) < 20:
                row_list.append(1)
            else:
                row_list.append(0)
                Squares_to_clear += 1
        bombfield.append(row_list)
    printfield(bombfield)


def printfield(bombfield):
    for row_list in bombfield:
        print(row_list)


def layout_window(window):
    for row_number, row_list in enumerate(bombfield):
        for column_number, column_entry in enumerate(row_list):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text="    ", bg="darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text="    ", bg="seagreen")
            else:
                square = tkinter.Label(window, text="    ", bg="green")
            
            square.grid(row = row_number, column = column_number)
            square.bind("<Button-1>", on_click)


def on_click(event):
    global score
    global game_Over
    global Squares_to_clear

    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])

    current_text = square.cget("text")

    if game_Over == False:
        if bombfield[row][column] == 1:
            game_Over = True
            square.config(bg = "red")
            print("Game Over! You hit a bomb!")
            print("Your score was: ", score)
        elif current_text == "    ":
            square.config(bg = "brown")
            total_bombs = 0

            if row < 9:
                if bombfield[row + 1][column] == 1:
                    total_bombs += 1
            if row > 0:
                if bombfield[row - 1][column] == 1:
                    total_bombs += 1
            if column > 0:
                if bombfield[row][column - 1] == 1:
                    total_bombs += 1
            if column < 9:
                if bombfield[row][column + 1] == 1:
                    total_bombs += 1

            if row > 0 and column > 0:
                if bombfield[row - 1][column - 1] == 1:
                    total_bombs += 1

            if row < 9 and column > 0:
                if bombfield[row + 1][column - 1] == 1:
                    total_bombs += 1

            if row > 0 and column < 9:
                if bombfield[row - 1][column + 1] == 1:
                    total_bombs += 1

            if row < 9 and column < 9:
                if bombfield[row + 1][column + 1] == 1:
                    total_bombs += 1
            
            square.config(text = " " + str(total_bombs) + " ")
            Squares_to_clear -= 1
            score += 1

            if Squares_to_clear == 0:
                game_Over = True
                print("Well done! You found all the safe square!")
                print("Your score was: ", score)


play_bombdodger()