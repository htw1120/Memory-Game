# Code partially written by Dr. Chad Mano of Utah State University
from modules.gameboard import GameBoard

def main():
    playerTurn = 0  # Keep track of whose turn it is

    print("Welcome to Memory\n")

    # Get the Board Size
    cols = int(input("Enter the number of columns on the board: "))
    rows = int(input("Enter the number of rows on the board: "))

    # Get the number of players
    playerCount = int(input("Enter the number of players: "))
    scores = [0] * playerCount

    # Create the MemoryBoard object
    memoryBoard = GameBoard(cols, rows)

    # Game loop
    winner = False
    while not winner:
        selectedCards = []  # Track the cards the current player selected
        printGameBoard(scores, memoryBoard.getBoard())

        # Each turn is two card flips
        for i in range(2):
            yPos, xPos = eval(input("Player " + str(playerTurn + 1) + " choose a card to flip (col, row): "))
            if memoryBoard.isCardFlipped(xPos, yPos):
                cardFlipped = True
                while cardFlipped:
                    yPos, xPos = eval(input("That card is already flipped over. Choose another card to flip: "))
                    if not memoryBoard.isCardFlipped(xPos, yPos):
                        cardFlipped = False
            selectedCards.append([xPos, yPos])
            memoryBoard.flipCard(xPos, yPos)
            printGameBoard(scores, memoryBoard.getBoard())

        # Player goes again if they get a match
        if memoryBoard.isMatch(selectedCards[0], selectedCards[1]):
            print("You got a match!")
            scores[playerTurn] += 1
            winner = sum(scores) == cols * rows // 2

            # If the game is over show a different message
            if winner:
                input("Hit Enter to Continue")
            else:
                playerTurn += 0
                input("Player " + str(playerTurn + 1) + " hit Enter to go again.")

        else:
            memoryBoard.flipCard(selectedCards[0][0], selectedCards[0][1])
            memoryBoard.flipCard(selectedCards[1][0], selectedCards[1][1])
            print("No Match")

            playerTurn += 1
            if playerTurn + 1 > playerCount:
                playerTurn = 0
            input("Hit Enter for Player " + str(playerTurn + 1))

    # Find the winning score value
    highScore = max(scores)

    # Check for a tie/winner
    if scores.count(highScore) > 1:
        print("The following players tied: ", end="")
        for i in range(len(scores)):
            if scores[i] == highScore:
                print((i + 1), end=" ")
    else:
        print("The winner is player " + str(scores.index(highScore) + 1))


# Print the scoreboard and gameboard
def printGameBoard(scores, board):
    #  os.system('cls||clear') # Comment this out if running in PyCharm
    for i in range(len(scores)):
        print("Player " + str(i + 1) + ": " + str(scores[i]))
    print()
    print(board)


main()
