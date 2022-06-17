
# Name : Arbaazkhan R S
# SRN : R20CS805

board = {
    'T1' : ' ', 'T2' : ' ','T3' : ' ',
    'M1' : ' ', 'M2' : ' ','M3' : ' ',
    'D1' : ' ', 'D2' : ' ','D3' : ' ',
}

player = 1            #  to initialize frst player
total_moves = 0       #  to count the moves
end_check = 0         #  to end the game


def check():
    # checking the moves of player 1


################################################################################

    # for horizontal(start) 

    if(board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X' ):
        print("Player one won !")
        return 1

    if(board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X' ):
        print("Player one won !")
        return 1

    if(board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X' ):
        print("Player one won !")
        return 1

    # for horiznontal(end)

###############################################################################


    # for diagonal (start) 

    if(board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X' ):
        print("Player one won !")
        return 1

    if(board['T3'] == 'X' and board['M2'] == 'X' and board['D1'] == 'X' ):
        print("Player one won !")
        return 1


    # for diagonal (end) 

###############################################################################

    # for vertical(start) 

    if(board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X' ):
        print("Player one won !")
        return 1

    if(board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X' ):
        print("Player one won !")
        return 1

    if(board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X' ):
        print("Player one won !")
        return 1

    # for vertical (end) 
 
##################################################################################
#**********************************************************************************


# checking the moves of player 2

############################################################################


# for horizontal(start) 

    if(board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O' ):
        print("Player one won !")
        return 1

    if(board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O' ):
        print("Player one won !")
        return 1

    if(board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O' ):
        print("Player one won !")
        return 1

# for horiznontal(end)

###########################################################################

# for diagonal (start) 

    if(board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O' ):
        print("Player one won !")
        return 1

    if(board['T3'] == 'O' and board['M2'] == 'O' and board['D1'] == 'O' ):
        print("Player one won !")
        return 1

# for diagonal (end) 

###########################################################################

# for vertical(start)

    if(board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O' ):
        print("Player one won !")
        return 1

    if(board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O' ):
        print("Player one won !")
        return 1

    if(board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O' ):
        print("Player one won !")
        return 1

        return 0

# for vertical (end) 

###########################################################################

print('T1|T2|T3')
print('--+--+--')
print('M1|M2|M3')
print('--+--+--')
print('D1|D2|D3')
print('--+--+--')

print('**********************************')

# to say the status of the board 
while True:
    print(board['T1'] + '|' + board['T2'] + '|' + board['T3'])
    print('--+--+--')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('--+--+--')
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])


    # storing the return value in end_check() 
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break

# to take the input from the user 
    while True:
        # Choosing a player 
        if player == 1:
            # Creating a new variable 
            p1 = input('Player one : ')
            if p1.upper() in board and board[p1.upper()] == ' ':
                    board[p1.upper()] = 'X'
                    player = 2
                    break

            # On Wrong input 

            else:
                print('Invalid Input, please try again')
                continue

        
        # Here player 2 
        else:
            p2 = input("player two : ")
            if p2.upper() in board and board[p2.upper()] == ' ':
                board[p2.upper()] = 'O'
                player = 1
                break

            else:
                print('Invalid Input, please try again')
                continue

total_moves = total_moves + 1
print('***********************************************')
print()