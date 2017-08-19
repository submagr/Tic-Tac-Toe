from __future__ import print_function
import numpy as np
from agent import Agent, HumanAgent, BotAgent 

class Board(object):
    '''
        tic tac toe board   
    '''
    def __init__(self, zero_symbol, cross_symbol, empty_symbol):
        self.board = np.zeros((3,3)) 
        self.players_labels = {zero_symbol: 1, cross_symbol:  -1, empty_symbol: 0}
        self.labels_players = {1: zero_symbol, -1: cross_symbol, 0: empty_symbol}
         
    def move(self, player_symbol, i, j):
        if self.board[i, j] != 0:
            return False
        self.board[i, j] = self.players_labels[player_symbol]
        return True

    def display(self):
        for i in range(3):
            print("\t\t", end="")
            for j in range(3):
                print(self.labels_players[self.board[i, j]] + "\t", end="")
            print()

    def __checkRow(self, i, j):
        return self.board[i, j] == self.board[i, (j+1)%3] and self.board[i, (j+1)%3] == self.board[i, (j+2)%3]

    def __checkCol(self, i, j):
        return self.board[i, j] == self.board[(i+1)%3, j] and self.board[(i+1)%3, j] == self.board[(i+2)%3, j]

    def __onDiag(self, i, j):
        return (i+j)==(3-1)

    def __checkDiag(self, i, j):
        if not self.__onDiag(i, j):
            return False
        n=3;
        isRightDiag =  (self.board[i, j] == self.board[(i+1)%n, (j+1)%n] and self.board[(i+1)%n, (j+1)%n] == self.board[(i+2)%n, (j+2)%n])
        isLeftDiag = (self.board[i, j] == self.board[(i+1)%n, (n+j-1)%n] and self.board[(i+1)%n, (n+j-1)%n] == self.board[(i+2)%n, (n+j-2)%n])
        return isLeftDiag or isRightDiag

    def checkMatch(self, i, j):
        if self.board[i, j] == 0:
            return 0
        return self.__checkRow(i, j) or self.__checkCol(i, j) or self.__checkDiag(i, j)

    def checkWin(self):
        if self.checkMatch(0,0):
            return self.board[0, 0]
        elif self.checkMatch(1,1):
            return self.board[1, 1]
        elif self.checkMatch(2,2):
            return self.board[2, 2]
        else:
            return 0 # Nobody won

    def isEmpty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    return True;
        return False;

    def is_over(self):
        winner = self.checkWin()
        if winner != 0:
            print("\t" + self.labels_players[winner], " won")
            return True 
        elif not self.isEmpty():
            print("\tdraw")
            return True
        return False

class BoardGame(object):
    '''
    '''
    def __init__(self, zero, cross):
        self.zero = zero
        self.cross = cross
        self.game_board = Board(zero.symbol, cross.symbol, "_")

    def move(self, player_symbol, i, j):
        if not self.game_board.move(player_symbol, i, j):
            return False
        return True

    def game_play(self):
        current_player = self.zero;
        while not self.game_board.is_over():
            i,j  = current_player.play();
            
            if self.move(current_player.symbol, i, j):
                self.game_board.display();
                if(current_player==self.zero):
                    current_player = self.cross
                else:
                    current_player = self.zero 
            else:
                print("\t( ", i , ", ", j, ") Already occupied")
