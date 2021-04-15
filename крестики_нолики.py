def main():
    board = [[], [], []]
    win = False
    while not win:
    display_board(board)
    player_step(board, "X")
    display_board(board)
    win = is_win(board)

    enemy_step(board, "0")


def display_board(board):
    for row in board:
        print(row)

def check_step(board, x, y):

    board[x][y]

def player_step(board, char):
    x = input()
    y = input()

def enemy_step():
    player_step(board, char)

def is_win(board): # как проверить

if __name__ == '__main__':
     main()