print("Hello from lesson 11_12_13")
def initboard():
    
    board = []

    for j in range(3):
        row = []
        for i in range(3):
            row.append(" ")
        board.append(row)

    return board

def printboard(argboard):
    count = 1
    for row in argboard:
        for cell in row:
            if cell == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {cell} ", end="")
            if count % 3 == 0:
                print("|")
                print("-"*13)
            
            count += 1

def get_play_move(argboard, player):
    move = input(f"Player {player}, make move (1-9):")

    if move.isdigit():
        move = int(move)
        if move > 0 and move < 10:
            move -= 1
            rowofmove = move // 3
            colofmove = move % 3
            
            argboard[rowofmove][colofmove] = player

            return argboard
        else:
            print("ONLY 1-9")
    else:
        print("NOT NUMBAH")


#----------------------------------------------------------------------------------MAIN-GAME-CODE------------------------------------------------------------------------------------------------

board = initboard()

printboard(board)

board = get_play_move(board, "X")

printboard(board)