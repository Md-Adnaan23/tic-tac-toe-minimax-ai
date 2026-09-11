#CODER CRYSTAL
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("CODER CATALYST")
root.geometry("500x600")
BG_COLOR = "#333333"
BUTTON_COLOR = "#FFFFFF" 
root.configure(bg=BG_COLOR)
root.resizable(0,0)

#Frame1
frame1 = Frame(root)
frame1.pack()
titlelabel1 = Label(frame1,text="TIC TAC TOE",font=("Arial",30,"bold"),bg="orange",relief="ridge",borderwidth="20")
titlelabel1.pack()

optionframe = Frame(root,bg=BG_COLOR)
optionframe.pack()

#Frame 2
frame2 = Frame(root,bg=BG_COLOR)
frame2.pack()

turn = "X"
game_end = False

mode = "Singleplayer"
def Singleplayer():
    global mode
    mode = "Singleplayer" 
    SingleplayerButton["bg"] = "green" 
    MultiplayerButton["bg"] = "light blue" 

def Multiplayer():
    global mode
    mode = "Multiplayer" 
    MultiplayerButton["bg"] = "green" 
    SingleplayerButton["bg"] = "light blue" 
    



board  = {1:"",2:"",3:"",
          4:"",5:"",6:"",
          7:"",8:"",9:""}
       




def win(player):
    #Rows
    if(board[1]==board[2] and board[2]==board[3] and board[3] == player):
        return True
    elif(board[4]==board[5] and board[5]==board[6] and board[6] == player):
        return True
    elif(board[7]==board[8] and board[8]==board[9] and board[9] == player):
        return True
    #Diagonals
    elif(board[1]==board[5] and board[5]==board[9] and board[9] == player):
        return True
    elif(board[3]==board[5] and board[5]==board[7] and board[7] == player):
        return True
    #Columns    
    elif(board[1]==board[4] and board[4]==board[7] and board[7] == player):
        return True    
    elif(board[2]==board[5] and board[5]==board[8] and board[8] == player):
        return True
    elif(board[3]==board[6] and board[6]==board[9] and board[9] == player):
        return True
    return False   

def draw():
    
    for i in  board.keys():
      if board[i] == "":
         return False
      
    return True  


def retry():
    global game_end,turn
    game_end = False
    turn = "X"
    button1["text"] = ""
    for button in buttons:
        button["text"] = " "
    for i in board.keys():    
        board[i] = ""

    for widget in frame2.winfo_children():
        if isinstance(widget, Label) and widget.cget("text") in ["X Wins the Game", "O Wins the Game", "Game Draw"]:
            widget.destroy()    

def minimax(board,isMaximizing):
    if win("O"):
        return 1
    if draw():     
        return 0
    if win("X"):
        return -1
    
    if isMaximizing:
        bestScore = -100


        for key in board.keys():
          if board[key] == "":
              board[key] = "O"
              score = minimax(board,False)
              board[key] = ""
              if score>bestScore :
                  bestScore = score
                 
        return bestScore
    else:
        bestScore = 100
 

        for key in board.keys():
          if board[key] == "":
              board[key] = "X"
              score = minimax(board,True)
              board[key] = ""
              if score<bestScore :
                  bestScore = score
                 
        return bestScore
        

def play_computer():
    bestScore = -100
    bestmove = 0

    for key in board.keys():
        if board[key] == "":
            board[key] = "O"
            score = minimax(board,False)
            board[key] = ""
            if score>bestScore :
                bestScore = score
                bestmove = key
 
    board[bestmove] = "O"
    buttons[bestmove - 1]["text"] = "O"  # Update the button text to show "O"
    print(f"Computer played at position {bestmove}")

    if win("O"):
        winningLabel = Label(frame2, text="O Wins the Game", bg="orange", font=("Arial", 32), width="14", height="2")
        winningLabel.grid(row=1, column=1, columnspan=3)
        game_end = True
    elif draw():
        drawLabel = Label(frame2, text="Game Draw", bg="red", font=("Arial", 32), width="14", height="2")
        drawLabel.grid(row=1, column=1, columnspan=3)
        game_end = True

    
    
  
     

def play(event):
    global turn,game_end
    if game_end:
        return
    
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n" :
        clicked = 1
    else:
        clicked = int(clicked)
    
    
    if button["text"] == " ":
      
   
      if turn == "X":
        button["text"] = "X"
        board[clicked] = turn
        if win (turn):
          winninglabel = Label(frame2,text=f"{turn} Wins the Game",bg="red",font=("Arial",32),width="14",height="2")
          winninglabel.grid(row = 1, column= 1, columnspan=3)
          game_end = True
        
        
                   
         
         
        turn = "O"
        if mode == "Singleplayer":
          play_computer()
          turn = "X"
        
        
        

        
      else:
        button["text"] = "O" 
        board[clicked] = turn
        if win (turn):
            winninglabel = Label(frame2,text=f"{turn} Wins the Game",bg="orange",font=("Arial",32),width="14",height="2")
            winninglabel.grid(row = 1, column= 1, columnspan=3)
            game_end = True
            
            
        turn = "X"
        
       
      if draw():
            drawLabel = Label(frame2,text=f"Game Draw",bg="red",font=("Arial",32),width="14",height="2")
            drawLabel.grid(row = 1, column= 1, columnspan=3)
            game_end = True
      print(f"Player X played at position {clicked}")     
    

SingleplayerButton = Button(optionframe, text="Singleplayer",bg="light blue",width="19",height="1",font=("Arial",10,"bold"),relief="raised",borderwidth="10",command=Singleplayer)
SingleplayerButton.grid(row=5,column=0,columnspan=1,sticky = "NW",padx=10,pady=10)   
MultiplayerButton = Button(optionframe, text="Multiplayer",bg="light blue",width="19",height="1",font=("Arial",10,"bold"),relief="raised",borderwidth="10",command=Multiplayer)
MultiplayerButton.grid(row=5,column=1,columnspan=1,sticky = "NW",padx=10,pady=10)       
 
# Row 1
button1 = Button(frame2,text= " ",width="4",height="2",font=("Arial\n",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button1.grid(row="0",column="1",padx=5,pady=5)
button1.bind("<Button-1>", play)
button2 = Button(frame2,text= " ",width="4",height="2",font=("Arial\n",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button2.grid(row="0",column="2",padx=5,pady=5)
button2.bind("<Button-1>", play)
button3 = Button(frame2,text= " ",width="4",height="2",font=("Arial\n",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button3.grid(row="0",column="3",padx=5,pady=5)
button3.bind("<Button-1>", play)
# Row 2
button4 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button4.grid(row="1",column="1",padx=5,pady=5)
button4.bind("<Button-1>", play)
button5 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button5.grid(row="1",column="2",padx=5,pady=5)
button5.bind("<Button-1>", play)
button6 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button6.grid(row="1",column="3",padx=5,pady=5)
button6.bind("<Button-1>", play)
# Row 3
button7 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button7.grid(row="2",column="1",padx=5,pady=5)
button7.bind("<Button-1>", play)
button8 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"",)
button8.grid(row="2",column="2",padx=5,pady=5)
button8.bind("<Button-1>", play)
button9 = Button(frame2,text= " ",width="4",height="2",font=("Arial",20),relief="raised",borderwidth="8",bg=BUTTON_COLOR)#FFFFFF"")
button9.grid(row="2",column="3",padx=5,pady=5)
button9.bind("<Button-1>", play)

#Row 5
restartButton = Button(frame2, text="Retry",bg="pink",width="45",height="1",font=("Arial",10,"bold"),relief="raised",borderwidth="8",command = retry)
restartButton.grid(row=5,column=1,columnspan=3,padx=5,pady=5)   
quitButton = Button(frame2, text="Quit Game", width=15, height=2, font=("Helec", 8,"bold"), bg="red", fg="black", relief=RAISED, borderwidth=2, command=root.destroy) 
quitButton.grid(row=6, column=2)


buttons = [button1,button2, button3,button4,button5,button6,button7,button8,button9]


root.mainloop()




''' 
Win func
print the no and dict
clicked n == 1
play func
print win in screen

 '''