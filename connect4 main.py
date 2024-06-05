# -*- coding: utf-8 -*-
"""

I have developed a Connect 4 game on python that implements; if/elif/else statements, functions, 
multiple variable types, operations, for and while loops, print and return statements, and file I/O. 
Connect 4 is a two player game so the program uses odd and even numbers to allow the users to take 
turns placing their chips on the game board. To personalize the game more, the program allows both 
users to enter a name along with the option to select different coloured chips. Using variable 
declaration for each column allows the program to keep track of the number of chips  on the 
board and whether the column or the entire board is full. After the game is over, the winner, 
loser and the duration of the game is written into the cps109_a1_output.txt file. However, 
the most challenging part is determining the winner since it is found by running through all 
possible ways, horizontally, vertically, and diagonally through the 7x6 board using for loops 
and list indexes to identify a sequence of four in a row.

""" 

import random
import time 


#creates a board using a list 
board = [[' A ','B ','C ',' D ',' E ','F ','G ']] #initial board contains column letter
for x in range(6):
    board.append(["⚫"] * 7) #creates a 7x6 board


#function for printing the list to form a board with the game title 
def print_board(board):  
    print('\n\n\n\t~ CONNECT FOUR ~')
    for row in board:
        print (" ".join(row))


#breaks down seconds into hours, min and remainder seconds  
def timer(sec):
  mins = sec // 60
  sec = sec % 60
  hours = int((sec // 60) // 60)
  mins = int((sec // 60) % 60)
  return (f'{hours}:{mins}:{sec:.2f}')


#function that generates different colour chips using file
def colourpick(n,ply,file_name):
    pick=1
    col=''

    while pick != 2:
        try:
            if pick==1:
                with open(file_name, "r") as file:
                    colours = file.readlines() #opens input file and chooses a random colour 
                
                #if choice is blank, re-asigns a new colour to variable 
                plycol= random.choice(colours).strip()
                if plycol==' ':
                    plycol= random.choice(colours).strip()
                elif plycol=='RED' and ply!="🔴":
                    col="🔴"
                elif plycol=='ORANGE' and ply!="🟠":
                    col="🟠"
                elif plycol=='YELLOW' and ply!="🟡":
                    col="🟡"
                elif plycol=='GREEN' and ply!="🟢":
                    col="🟢"
                elif plycol=='BLUE' and ply!="🔵":
                    col="🔵"
                elif plycol=='PURPLE' and ply!="🟣":
                    col="🟣"               
            elif pick!=2:      
                print("\033[1;31;49mInvalid Input. Please try again.\n\033[1;37;49m")
            
            #either continues to generate or moves on 
            pick = int(input(f"\n{n}: {col}\nEnter 1 to generate a new colour. Enter 2 to continue >> "))

        #if pick value entered is not a int, asks to re-enter rather than stopping game 
        except ValueError:
            print("\033[1;31;49mInvalid Input. Please try again.\n\033[1;37;49m")
    return col


#function that allows player 1 & 2 to pick a name which cannot be the same 
def name(n,pnam):

    name = input(f"Player {n}: Enter your name >> ")
    while name=="" or name==pnam:
        if name==pnam:
            name = input(f"\033[1;31;49mDon't copy Player 1. Be creative! Please try again.\n\033[1;37;49mPlayer {n}: Enter your name >> ")
        elif name=="":
            name = input(f"\033[1;31;49mName is blank. Please try again.\n\033[1;37;49mPlayer {n}: Enter your name >> ")
    return name
 
    
#function that saves game outcome to file 
def win_stats(filename,winner,loser,time):
    with open(filename, "a") as file:
        file.write(f"WINNER: {winner}\tLOSER: {loser}\t\tTIME: {time}\n")
    
 
#check through the game board for a four in a row   
def checker(chip,name):
    
    row=6
    column=7
            
    #checks rows from left to right starting with bottom row 
    for x in range(column-3):
        for y in range(row,0,-1):
            if (board[y][x]==chip and board[y][x+1]==chip and board[y][x+2]==chip and board[y][x+3]==chip):
                print("Game Over", name, "Wins!")
                return True 
            
    #checks columns from the botom of the column  to the top     
    for x in range(column):
        for y in range(row,0,-1):
            if (board[y][x]==chip and board[y-1][x]==chip and board[y-2][x]==chip and board[y-3][x]==chip):
                print("Game Over", name, "Wins!")
                return True 
     
    #check diagonal from bottom left to top right        
    for x in range(column-3):
        for y in range(row,0,-1):
            if (board[y][x]==chip and board[y-1][x+1]==chip and board[y-2][x+2]==chip and board[y-3][x+3]==chip):
                print("Game Over", name, "Wins!")
                return True                           
    
    #checks diagonal from bottom right to top left       
    for x in range(3,column):
        for y in range(row,0,-1):

            if (board[y][x]==chip and board[y-1][x-1]==chip and board[y-2][x-2]==chip and board[y-3][x-3]==chip):
                print("Game Over", name, "Wins!")
                return True   
            
    #if there is no 4 in row, continue to play     
    return False    


#function to place a chip 
def chip_place(name,chip,A,B,C,D,E,F,G):
    place = input(f"{name}'s Turn\ncolumn >> ") 
    place = place.upper()
    
    #if the column entered is not in the range of columns included the board
    while place!='A' and place!='B' and place!='C' and place!='D' and place!='E' and place!='F' and place!='G':
        place = input("\033[1;31;49mInvalid Input. Please try again.\n\033[1;37;49m\nColumn >> ")
        place = place.upper()
    
    #when user enteres a valid choice that is included in the board
    if place=='A' and A>0:
        board[A][0]=chip
        A-=1

        
    elif place=='B' and B>0:
        board[B][1]=chip
        B-=1

    elif place=='C' and C>0:
        board[C][2]=chip
        C-=1
        
    elif place=='D' and D>0:
        board[D][3]=chip
        D-=1

    elif place=='E' and E>0:
        board[E][4]=chip
        E-=1

    elif place=='F' and F>0:
        board[F][5]=chip
        F-=1
        
    elif place=='G' and G>0:
        board[G][6]=chip
        G-=1
    else: 
        print("Column full, choose another")
        return chip_place(name,chip,A,B,C,D,E,F,G) #runs the function again to allow the user to choose another column
    
    print_board(board)
    return A, B, C, D, E, F, G #returns udates variable value after turn 


def connect4():
    output_file = 'cps109_a1_output.txt' #creates a txt file to save game winner/loser data in the win_stats function 
    input_file = 'colours.txt' #a txt file that contains multiple colours which is used for the colourpick function
    A=6
    B=6
    C=6 
    D=6
    E=6 
    F=6
    G=6  
    turn=1 #records the amount of turn 
    p1_win=False 
    p2_win=False
    p1name= name(1,0) #runs name fuction to asign player 1 a name 
    p2name= name(2,p1name) #runs name fuction to asign player 2 a name 
    
    p1col=colourpick(p1name,0,input_file) #runs colour fuction to asign player 1 a colour chip 
    p2col=colourpick(p2name,p1col,input_file) #runs colour fuction to asign player 2 a colour chip 
    print_board(board)
    start_time = time.time()

    play=True 
    while play is True:
        
        if (turn%2)==1:
            A, B, C, D, E, F, G = chip_place(p1name,p1col, A, B, C, D, E, F, G)
        elif (turn%2)==0:
            A, B, C, D, E, F, G = chip_place(p2name,p2col, A, B, C, D, E, F, G)
            
        turn+=1
        if checker(p1col, p1name):
            p1_win=True
            break

        elif checker(p2col, p2name):
            p2_win=True
            break

        elif A+B+C+D+E+F+G == 0:
            print('It''s a Tie')
            break
    
    #timer 
    end_time = time.time()#stops the timer 
    tot_time = end_time - start_time #find the total time the code ran
    gametime = timer(tot_time) #usses tot_time function to convert sec to hour:min:sec
    
    if p1_win is True: #if player 1 wins
        win_stats(output_file, p1name,p2name, gametime)
    elif p2_win is True: #if player 2 wins
        win_stats(output_file,p2name,p1name, gametime)

if __name__ == "__main__":
    connect4()