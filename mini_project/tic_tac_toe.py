import termcolor

board = list(range(1, 10))
plyer, computer = "X", "O"
movement_win = ((0, 4, 8), (2, 4, 6), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8))
move_computer = ((1, 3, 7, 9), (5,), (2, 4, 8, 6))


def color_board(item, end):
    if item == plyer:
        print(termcolor.colored(f"[{item}]", "red"), end=end)
    elif item == computer:
        print(termcolor.colored(f"[{item}]", "blue"), end=end)
    else:
        print(f"[{item}]", end=end)


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        color_board(i, end)
        j += 1


def has_empty_space():
    return board.count(plyer) + board.count(computer) != 9


print(f"Player : {plyer}\nComputer : {computer}\n")


def can_move(board, move):
    if move in range(1, 10) and isinstance(board[move - 1], int):
        return True
    return False


def is_winner(board, plyer):
    for tup in movement_win:
        win = True
        for j in tup:
            if board[j] != plyer:
                win = False
                break
        if win: break
    return win


def make_move(board, user, move, undo=False):
    if can_move(board, move):
        board[move - 1] = user
        win = is_winner(board, user)
        if undo:
            board[move - 1] = move
        return True, win
    else:
        return False, False


def computer_move():
    mv = -1
    # if computer can winner
    for i in range(1, 10):
        # [1] => can win on make_move return
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # if player can winner ,computer stop it
    for j in range(1, 10):
        if make_move(board, plyer, j, True)[1]:
            mv = j
            break
    # normal computer move
    if mv == -1:
        for tup in move_computer:
            for mov in tup:
                if mv == -1 and can_move(board, mov):
                    mv = mov
                    break
    return make_move(board, computer, mv)


while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, plyer, move)
    if not moved:
        print("Invalid number! Try again!")
        continue
    if won:
        print(termcolor.colored("You Winner!!", "green"))
        break
    elif computer_move()[1]:
        print(termcolor.colored("You lose!!", "red"))
        break
print_board()
