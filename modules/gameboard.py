from modules.memorycard import MemoryCard
from random import shuffle

class GameBoard:
    def __init__(self,COLS, ROWS):
        self.__cols = COLS
        self.__rows = ROWS
        self.__board = []
        firstList = []
        for x in range((self.__cols * self.__rows)):
            firstList.append(MemoryCard(x))
        shuffle(firstList)
        for i in range(self.__rows):
            self.__board.append([])
        for j in range(self.__rows):
            for k in range(self.__cols):
                self.__board[j].append(firstList.pop())
    def getBoard(self):
        gameBoardDisplay = " "
        for i in range(self.__cols):
            gameBoardDisplay += " | " + str(i + 1)
        gameBoardDisplay += " |"
        for j in range(self.__rows):
            gameBoardDisplay += "\n-" + "-----"* self.__cols
            gameBoardDisplay += "\n" + str(j + 1) + " | "
            for k in range(self.__cols):
                gameBoardDisplay += str(self.__board[j][k].displayCard())
                gameBoardDisplay += " | "
        return gameBoardDisplay
    def flipCard(self, xPos, yPos):
        self.__board[xPos-1][yPos-1].toggleFlipped()
    def isCardFlipped(self, xPos, yPos):
        if self.__board[xPos-1][yPos-1].isFlipped()==True:
            return True
        else:
            return False
    def isMatch(self, pos1, pos2):
        xPos = pos1[0] 
        yPos = pos1[1] 
        xPos1 = pos2[0] 
        yPos1 = pos2[1] 
        if self.__board[xPos-1][yPos-1].getValue() == self.__board[xPos1-1][yPos1-1].getValue():
            return True
        else:
            return False
   