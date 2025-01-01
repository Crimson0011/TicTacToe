import tkinter

def set_tile(row,column):
    global current_player

    if(game_over):
        return

    if board[row][column]["text"] !="":
        return

    board[row][column]["text"] = current_player

    if current_player == player_1:
        current_player = player_2
    else :
        current_player = player_1

    label["text"] = current_player+"'s turn"
    winner()

def winner():
    global turns, game_over
    turns += 1

#แนวตั้ง
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] !=""):
            label.config(text=board[row][0]["text"]+" is the winner!!!" , foreground=color_purple)
            for column in range(3):
                board[row][column].config(foreground="yellow", background="gray")
            game_over = True
            return
#แนวนอน
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] !=""):
            label.config(text=board[column][0]["text"] + " is the winner!!!", foreground=color_purple)
            for row in range(3):
                board[row][column].config(foreground="yellow", background="gray")
            game_over = True
            return
#แนวเฉียง
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] !=""):
        label.config(text=board[0][0]["text"] + " is the winner!!!", foreground=color_purple)
        for i in range(3):
            board[i][i].config(foreground="yellow", background="gray")
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!!!", foreground=color_purple)
        board[0][2].config(foreground="yellow", background="gray")
        board[1][1].config(foreground="yellow", background="gray")
        board[2][0].config(foreground="yellow", background="gray")
        game_over = True
        return

    if (turns == 9):
        game_over = True
        label.config(text="Draw!!!" , foreground=color_purple)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label["text"] = current_player+"'s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_purple, background="black")

player_1 = "X"
player_2 = "O"
current_player = player_1
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_darkblue = "#00008B"
color_purple = "#800080"
color_black = "black"
color_white = "#FFFFFF"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("TicTacToe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn", font=("Terminal", 20, "bold"), background="black"
                      ,foreground=color_purple)

label.grid(row=0, column=0 , columnspan=3 , sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Arial", 50, "bold"),
                                         background="black", foreground=color_purple, width=4, height=1,
                                         command=lambda r=row, c=column: set_tile(r,c))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Terminal", 20, "bold"), background=color_black,foreground=color_purple, command = new_game)

button.grid(row=4, column=0, columnspan=3 , sticky="we")

button.grid(row=4, column=0)

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
