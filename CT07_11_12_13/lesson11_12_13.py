print("Hello from lesson 11_12_13")
def initboard():
    
    board = []

    for j in range(3):
        row = []
        for i in range(3):
            row.append(" ")
        board.append(row)

    return board

#----------------------------------------------------------------------------------MAIN-GAME-CODE------------------------------------------------------------------------------------------------

board = initboard()

print(board)