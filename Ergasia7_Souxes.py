import random
import time

marker = {'Player 1': 'X', 'Player 2': 'O', }

def display_board(board): 
    print('-------------')
    print('|7  |8  |9  |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9]+' |')
    print('|   |   |   |')
    print('-------------')
    print('|4  |5  |6  |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6]+' |')
    print('|   |   |   |')
    print('-------------')
    print('|1  |2  |3  |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3]+' |')
    print('|   |   |   |')
    print('-------------')

def choose_first():
    arithmos = random.randint(1,2)
    if arithmos == 1 :
        player = 'Player 1'
    else:
        player = 'Player 2'
    return player

def display_score(score):
    print ("The score is: {} ".format(score))

def place_marker(board, marker, position): 
    board[position] = marker
        

def win_check(board,mark): 
    if board[1] == board[2] == board[3] == mark :
        return True
    elif board[4] == board[5] == board[6] == mark :
        return True
    elif board[7] == board[8] == board[9] == mark :
        return True
    elif board[1] == board[4] == board[7] == mark :
        return True
    elif board[2] == board[5] == board[8] == mark :
        return True
    elif board[3] == board[6] == board[9] == mark :
        return True
    elif board[3] == board[5] == board[7] == mark :
        return True
    elif board[1] == board[5] == board[9] == mark :
        return True
    else:
        return False
    
def board_check(board): 
    if board[1] == ' ' or board[2] == ' ' or board[3] == ' ' or board[4] == ' ' or board[5] == ' ' or board[6] == ' ' or board[7] == ' ' or board[8] == ' ' or board[9] == ' '  :
        return False
    else :
        return True
    
 
def player_choice(board, turn): 
    epilogi = input("What's your move? (1-9) : {} ".format(turn))
    while True :
        if epilogi not in '1 2 3 4 5 6 7 8 9'.split() :
            epilogi = input("What's your move?  (1-9) : {} ".format(turn))
            continue
        else :
            if board[int(epilogi)] != ' ' :
                print("This block is taken,try again")
                epilogi = input("What's your move?  (1-9) : {} ".format(turn))
                continue
            else :
                return int(epilogi)



def replay():
    epilogi = input("Do you want to play again?  Yes/No ")
    if epilogi == 'Yes' or epilogi == 'yes':
            return True
    else:
            return False
    

def next_player(turn):
    if turn == 'Player 1' :
        return 'Player 2'
    else:
        return 'Player 1'

def main():
    score = {} 
    print('The draw is starting! ')
    for i in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    turn = choose_first() 
    print(turn + ' is playing first:')
    first = turn 
    game_round = 1
    while True:
        theBoard = [' '] * 10 
        game_on = True
        while game_on:
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): 
                display_board(theBoard)
                print('The winner is '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Tie!')
                game_on = False
            else: 
                turn = next_player(turn)
        if not replay():
            if game_round>1 : ending = ''
            print("Thank you for playing")
            format(game_round, ending)
            display_score(score) 
            break
        else :
            game_round += 1
            turn = next_player(first) 
            first = turn
main()
