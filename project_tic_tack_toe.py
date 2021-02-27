#!/usr/bin/env python
# coding: utf-8

# In[3]:


board=[' ']*10


# In[4]:


# STEP1:- DISPLAYING BOARD FUNCTION
from IPython.display import clear_output
def display_board(board):
    clear_output()                        # to clean previous output
    print(board[7]+' | '+board[8]+ ' | ' +board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])


# In[5]:


display_board(board)


# In[6]:


# STEP2:- CHOOSING MARKER FOR PLAYER1 AND PLAYER2
def player_input():
    marker=' '
    while marker!= 'X' and marker!='O':
        marker= input("Player1,Enter 'x' or 'o': ").upper()
        player1= marker
        if player1=='X':
            player2='O'
        else:
            player2='X'
            
    return (player1,player2)


# In[7]:


player_input()


# In[8]:


player1_marker,player2_marker= player_input() # so now we can know who's marker is 'x' and whose 'o' 


# In[9]:


player2_marker


# In[10]:


#STEP 3:- ASSIGNING WHO WILL GO FIRST PLAYER1 OR PLAYER2
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'


# In[11]:


choose_first()


# In[12]:


#STEP 4:- TAKING MARKER AND ASSIGNING IT TO THE DESIRED POSITION
def place_marker(board,marker,position):
    board[position]=marker


# In[13]:


place_marker(board,'$',4)


# In[14]:


display_board(board)


# In[15]:


#STEP 5:- FUNCTION TO CHECK WHO WON THE MATCH according to player1 or player2 input
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[16]:


#STEP 6:- FUNCTION TO CHECK ANY FREE SPACE AVAILABLE ON BOARD, if no space draw else player2 turn 
def space_check(board,position):
    return board[position]==' '   


# In[17]:


#STEP 7:- FUNCTION TO CHECK IF THE BOARD IS FULL & RETURNS A BOOLEAN VALUE TRUE IF FULL, FALSE OTHERWISE
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[18]:


#STEP 8:- FUNCTION THAT ASK PLAYER FOR NEXT POSTION FROM 1-9,and using space_check function can know the empty space 

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input("enter the next position in 1-9: "))
    return position


# In[19]:


#STEP 9:- FUNCTION TO ASK PLAYER IF THEY WANT TO PLAY GAME AGAIN OR NOT
def replay():
    return input('Do you want to play again yes/no: ').lower().startswith('y')


# In[ ]:


print("welcome to tick tac toe game")
while True:
    #Reseting board
    theboard= [' ']*10
    player1_marker,player2_marker=player_input()    # taking player1 and player2 marker
    turn= choose_first()                            # random generator of first player
    print(turn+' will go first')
    
    # Now asking if players are ready to play or not
    
    play_game= input('Are you ready to play y/n: ')
    if play_game.lower()[0]== 'y':
        game_on= True
    else:
        game_on= False
    
    # so if players are ready starting the game
    while game_on:                                 # if game_on True it will enter in while loop else not
        
        # there can be two conditions either player 1 have turn or player 2 have
        # if turn== player1 else turn== player2  
        
        if turn== 'player1':
            
            display_board(theboard)                                         #displaying board
            position = player_choice(theboard)                              #choosing next position
            place_marker(theboard, player1_marker, position)                # marking at desired position
            
            if win_check(theboard,player1_marker)==True:
                display_board(theboard)
                print('Congratulation!! player1 won the game')
                game_on= False                                              # so it will not enter again in while loop
            else:
                if full_board_check(theboard)==True:
                    display_board(theboard)
                    print('Its a draw...')
                    break
                else:
                    turn ='player2'
        else:
            
            #player2 turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player1'
    if not replay():
        break
                    


# In[ ]:




