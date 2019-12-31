#lists and strings which are needed to be defined
mylist = [' ']*9

#functions
def game_board():
    print(' ')    
    print(f' {mylist[6]} | {mylist[7]} | {mylist[8]}')
    print(f'-----------')
    print(f' {mylist[3]} | {mylist[4]} | {mylist[5]}')
    print(f'-----------')
    print(f' {mylist[0]} | {mylist[1]} | {mylist[2]}')
    print(' ')
    
def intro_board():
    print(' ')
    print(f' 7 | 8 | 9')
    print(f'-----------')
    print(f' 4 | 5 | 6')
    print(f'-----------')
    print(f' 1 | 2 | 3')
    print(' ')
         
def input_p1():
    while True:
        try:
            i = int(input('please enter a number between 1-9: '))
            if i not in range(1,10):
                print('please enter a number between 1-9: ')
                continue
            else:
                pass
        except ValueError:
            print("You are supposed to enter a number between 1-9. Try Again: ")
            continue
        
        i = i - 1
        if mylist[i] == "X" or mylist[i] == "O" and i <= 9:
            print("This place have been already been occupied by", mylist[i])

        elif x == 'Player1':
            mylist[i] = 'X'
            game_board()

            undo = input('to finalize press enter or else press u to undo the move: ')
            undo = undo.upper()
            if undo == 'U':
                mylist[i] = ' '

            else:
                game_board()
                break    
        elif o == 'Player1':
            mylist[i] = 'O'
            game_board()

            undo = input('to finalize press enter or else press u to undo the move: ')
            undo = undo.upper()
            if undo == 'U':
                mylist[i] = ' '
            else:
                game_board()
                break         

def input_p2():
    while True:
                
        try:
            j = int(input("please enter a number between 1-9: "))
            if j not in range(1,10):
                print('please enter a number between 1-9: ')
                continue
            else:
                pass
        except ValueError:
            print("You are supposed to enter a number between 1-9. Try Again: ")
            continue
        
        j = j -1
        if mylist[j] == "X" or mylist[j] == "O" and j <= 9:
            print("This place have been already been occupied by", mylist[j])

        elif x == 'Player2':
            mylist[j] = 'X'
            game_board()

            undo = input('to finalize press enter or else press u to undo the move: ')
            undo = undo.upper()
            if undo == 'U':
                mylist[j] = ' '
            else:
                game_board()
                break    
            
        elif o == 'Player2':
            mylist[j] = 'O'
            game_board()

            undo2 = input('to finalize press enter or else press u to undo the move: ')
            undo2 = undo2.upper()
            if undo2 == 'U':
                mylist[j] = ' '
            else:
                game_board()
                break
            
def check_win():
    if mylist[0] == mylist[1] == mylist[2] != ' ' or mylist[3] == mylist[4] == mylist[5] != ' ' or mylist[6] == mylist[7] == mylist[8] != ' ' or mylist[0] == mylist[4] == mylist[8] != ' ' or mylist[6] == mylist[4] == mylist[2] != ' ' or mylist[6] == mylist[3] == mylist[0] != ' ' or mylist[7] == mylist[4] == mylist[1] != ' ' or mylist[8] == mylist[5] == mylist[2] != ' ': 
        return 'wins'
    elif ' ' not in mylist:
        return 'draws'

#Start of the game
print("Welcome to play the game TicTacToe get to continue ")

while True:

    player_choice = input('Player one, do you want to choose "X" or "O": ')
    player_choice = player_choice.upper()

    intro_board()
    if player_choice == 'X':
        x  = 'Player1'
        o = 'Player2'
        print('So player 1 is assigned "X" and player 2 is assigned "O"')
        break
    elif player_choice == 'O':
        x = 'Player2'
        o = 'Player1'
        print('So player 1 is assigned "O" and player 2 is assigned "X"')
        break
    else:
        print('I think you are supposed to enter either "X" or "O" \nTry again')
        continue

print('This is how you give input to the board')
    
while True:
    # game_board()
    # print(' please enter a number between 0-9 as seen in the numberpad')
    
    input_p1()

    if check_win() == 'wins':
        print(f"the player 1 wins")
        break
    
    elif check_win() == 'draws':
        print('well its a tie')
        break
    
    input_p2()

    if check_win() == 'wins':
        print(f"the player 2 wins")
        break
    
    elif check_win() == 'draws':
        print('well its a tie')
        break