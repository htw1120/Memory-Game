from random import randint


class MemoryCard:
    def __init__(self, id):
        self.__firstAscii = 33
        self.__id = id
        self.__flipCard = False
        self.__value = self.getValue()

    def getValue(self):
        newValue = self.__id
        if self.__id % 2 != 0:
            newValue -= 1
        return newValue + self.__firstAscii

    def toggleFlipped(self):
        if self.__flipCard == True:
            self.__flipCard = False
            return False
        if self.__flipCard == False:
            self.__flipCard = True
            return True

    def isFlipped(self):
        if self.__flipCard == True:
            return True

    def displayCard(self):
        if self.__flipCard == True:
            return str(chr(self.getValue()))
        else:
            return str(" ")

    def __str__(self):
        return self.displayCard()
