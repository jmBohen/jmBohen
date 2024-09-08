"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_delta = 0

    for row in board:
        for cell in row:
            match cell:
                case None:
                    continue
                case X:
                    count_delta += 1
                case O:
                    count_delta -= 1
    if count_delta == 0:
        return X
    else:
        return O


def actions(board):
    actions = set()
    for row in board:
        for cell in row:
            if cell == None:
                actions.add((row, cell))
    return actions
    


def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")
    else:
        board_copy = board
        board_copy[action[0]][action[1]] = player(board)
        return board_copy


def winner(board):
    h = winner_horizontally(board)
    v = winner_vertically(board)
    d = winner_diagonally(board)
    if h != None: return h
    elif v != None: return v
    elif d != None: return d
    else: return None


def winner_horizontally(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    return None

def winner_vertically(board):

    for _ in range(3):
        if board[0][_] == board[1][_] == board[2][_]:
            return board[0][_]
    return None

def winner_diagonally(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][3] == board[1][1] == board[2][0]:
        return board[1][1]
    else:
        return None

def terminal(board):
    if not winner(board) == None:
        return True 

    for row in board:
        for cell in row:
            if cell == Empty:
                return False

    return True


def utility(board):
    result = winner(board)

    match result:
        case None: return 0
        case X: return 1
        case O: return -1

def minimax(board):
    player = player(board)
    actions = actions(board)

    best_action = actions[0]
    
    match player:
        case X:
            best_value = -math.inf
            for action in actions:
                value = max_value(result(board, action)) 
                if  value > best_value:
                    best_action = action
                    best_value = value
            return best_action
        case O:
            best_value = math.inf
            for action in actions:
                value = min_value(result(board, action)) 
                if  value < best_value:
                    best_action = action
                    best_value = value
            return best_action

def max_value(board):
    maksimum = -math.inf


    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        minimum = min_value(result(board, action)) 
        if not  minimum > maksimum:
            continue
        maksimum = minimum
    
    return maksimum

def min_value(board):
    minimum = math.inf


    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        maksimum = max_value(result(board, action)) 
        if not  maksimum < maks:
            continue
        minimum = maksimum
    
    return minimum