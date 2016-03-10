# Kyle O'Connor kyjoconn@ucsc.edu assignment 5 'Connect 5'
def make_matrix():
    """ I made this function to make my board, it's not actually used in the game """
    matrix = [[' '] * 9] * 7 + [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    for row in matrix:
        print ' '.join(row)


def make_move_x(matrix, choice):
    """ This function takes a matrix, finds an open blank space
        on the board in the selected column and replaces it with an X """
    for i in range(1, 9):
        if matrix[-i][choice - 1] == ' ':
            matrix[-i][choice - 1] = 'X'
            return matrix


def make_note(matrix, choice):
    """ This function does just what make_move_x does except it identifies the row that make_move_x will act on """
    #I made this function to help check for diagonal wins
    note = 0
    for i in range(1, 9):
        if matrix[-i][choice - 1] == ' ':
            note += i
            break
    return note


def make_move_o(matrix, choice):
    """ This function takes a matrix, finds an open blank space
        on the board in the selected column and replaces it with an O """
    for i in range(1, 9):
        if matrix[-i][choice - 1] == ' ':
            matrix[-i][choice - 1] = 'O'
            return matrix

if __name__ == "__main__":
    # test and turn are initialized here so I can break out of 'while test == 0' later,
    # and turn is for alternating player turns
    test = 0
    turn = 1
    # these are the matrices I used to get going (made from first function make_matrix)
    matrix_o = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    matrix_x = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    while test == 0:
        #print blank board
        if turn == 1:
            for row in matrix_o:
                print ''.join(row)
                print ' '
        #player X's turn
        if turn in range(1, 200, 2):
            # initialize vert_list so I can later check for a vertical win
            # add one to turn so that it will alternate to player O after player X
            vert_list = []
            turn += 1
            # this for loop asks for which column to play, and makes sure all the input is valid
            for tries in range(10):
                choice = raw_input('Player X, which column do you wish to play (1-9)? ')
                print ''
                if tries == 9:
                    choice = None
                    break
                elif len(choice) != 1:
                    pass
                elif choice not in '123456789':
                    pass
                elif matrix_x[0][int(choice) - 1] != ' ':
                    print 'Column full, try another'
                    pass
                elif len(choice) == 1:
                    if choice in '123456789':
                        break
            #now with the valid input, player X can make his/her turn in the column of their choice
            #and make_note keeps track of which row is played
            #also initialize diagonal counts for later use
            if choice != None:
                choice = int(choice)
                note = make_note(matrix_o, choice)
                matrix_x = make_move_x(matrix_o, choice)
                diag_count = 0
                diag_2_count = 0
                #print the new board
                for row in matrix_x:
                    print ''.join(row)
                print ''
                #check for vert win
                for i in range(7):
                    vert_list.append(matrix_x[i][choice - 1])
                vert_list = ''.join(vert_list)
                if 'XXXXX' in vert_list:
                    print 'Game over Player X wins (vertically)'
                    #add one to test so that the loop will break if player X has won
                    test += 1
                #check for horizontal win
                for row in matrix_x:
                    row = ''.join(row)
                    if 'XXXXX' in row:
                        print 'Game over Player X wins (horizontally)'
                        test += 1
                #check for diagonal win (first direction)
                #restrictions on choice and note(row just played) to avoid list out of range errors
                if choice >= 5 and note > 5:
                    for i in range(5):
                        if matrix_x[-note + i][choice - 1 - i] == matrix_x[-note][choice - 1] and matrix_x[-note][
                                    choice - 1] != ' ':
                            diag_count += 1
                if diag_count == 5:
                    test += 1
                    print 'Game over Player X wins (diagonally)'
                #same thing but diagonal (second direction)
                if choice <= 5 and note > 5:
                    for i in range(5):
                        if matrix_x[-note + i][choice - 1 + i] == matrix_x[-note][choice - 1] and matrix_x[-note][
                                    choice - 1] != ' ':
                            diag_2_count += 1
                if diag_2_count == 5:
                    test += 1
                    print 'Game over Player X wins (diagonally)'
            #break out of loop if player x has won
            if test == 1:
                break
            #if the every column is full and no one has won, call it a draw
            if test != 1:
                if ' ' not in matrix_x[0]:
                    print 'Draw'
                    break
        #Now does the exact same thing for player O
        if turn in range(2, 200, 2):
            vert_list = []
            o_count = []
            turn += 1
            for tries in range(10):
                choice = raw_input('Player O which column do you wish to play (1-9)? ')
                print ''
                if tries == 9:
                    choice = None
                    break
                elif len(choice) != 1:
                    pass
                elif choice not in '123456789':
                    pass
                elif matrix_o[0][int(choice) - 1] != ' ':
                    print 'Column full, try another'
                    pass
                elif len(choice) == 1:
                    if choice in '123456789':
                        break
            if choice != None:
                choice = int(choice)
                matrix_o = make_move_o(matrix_x, choice)
                note = make_note(matrix_x, choice) - 1
                diag_count = 0
                diag_2_count = 0
                for row in matrix_o:
                    print ''.join(row)
                print ''
                for i in range(7):
                    vert_list.append(matrix_o[i][choice - 1])
                vert_list = ''.join(vert_list)
                if 'OOOOO' in vert_list:
                    test += 1
                    print 'Game over Player O wins (vertically)'
                for row in matrix_o:
                    row = ''.join(row)
                    if 'OOOOO' in row:
                        test += 1
                        print 'Game over Player O wins (horizontally)'
                        break
                if choice >= 5 and note > 5:
                    for i in range(5):
                        if matrix_x[-note + i][choice - 1 - i] == matrix_x[-note][choice - 1] and matrix_x[-note][
                                    choice - 1] != ' ':
                            diag_count += 1
                if diag_count == 5:
                    test += 1
                    print 'Game over Player O wins (diagonally)'
                if choice <= 5 and note > 5:
                    for i in range(5):
                        if matrix_x[-note + i][choice - 1 + i] == matrix_x[-note][choice - 1] and matrix_x[-note][
                                    choice - 1] != ' ':
                            diag_2_count += 1
                if diag_2_count == 5:
                    test += 1
                    print 'Game over Player O wins (diagonally)'
                if test == 1:
                    break
                if test != 1:
                    if ' ' not in matrix_x[0]:
                        print 'Draw'
                        break


