import numpy as np
import time

class bingob:
    def __init__(self,string_list):
        self.board = np.zeros([5,5], dtype = np.int8)
        self.drawn = np.zeros([5,5], dtype = np.int8)
        
        for i in range(5):
            strings = string_list[i].split(' ')
            #remove empty strings
            strings = [string for string in strings if string != '']
            self.board[i,:] = np.array([int(string) for string in strings])
        
    def register_number(self, number):
        for row,col in np.ndindex(5,5):
            if self.board[row,col] == number:
                self.drawn[row,col] = 1
                                
    def check_winner(self):
        #check rows
        for row in np.ndindex(5):
            if self.drawn[row,:].all():
                return True
        #check cols
        for col in np.ndindex(5):
            if self.drawn[:,col].all():
                return True
        # if not...
        return False
    
    def sumofnotdrawn(self):
         return (self.board * (1 - self.drawn)).sum()

    def reset(self):
        self.drawn = np.zeros([5,5], dtype = np.int8)
        

def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def get_stuff(filename):
    lines = get_lines(filename)
    drawn = lines[0].split(',')
    drawn = [int(i) for i in drawn]
    boardstrings = lines[1:]
    boards = get_boards(boardstrings)
    return drawn, boards

def get_boards(boardstrings):
    boards = []
    starts_at = 1
    while True:
        try:            
            boards.append(bingob(boardstrings[starts_at:starts_at+5]))
            starts_at += 6;
        except:
            break
    return boards

def play_bingo(drawn,boards):
    winners = []
    for number in drawn:
        for board in boards:
            board.register_number(number)
        for board in boards:
            if board.check_winner():
                winners.append(board)
        if len(winners) == 1:
            return winners[0], number
        if len(winners) > 1:
            print("Several winners")
            return winners, number

def find_loser(drawn,boards):
    for number in drawn:
        losers = []
        for board in boards:
            board.register_number(number)
        for board in boards:
            if not(board.check_winner()):
                losers.append(board)
        if len(losers) == 1:
            return losers[0]


if __name__ == '__main__':

    start_time = time.time()

    filename = '04a_input.txt'
    drawn, boards = get_stuff(filename)
        
    print("\nPart1")
    winner, number = play_bingo(drawn,boards)
    print('sum of not drawn: ', winner.sumofnotdrawn())
    print('final number: ', number)
    print('answer: ', winner.sumofnotdrawn() * number)

    print("\nPart2")
    for board in boards:
        board.reset()
    loser = find_loser(drawn,boards)
    loser.reset()
    loser, number = play_bingo(drawn,[loser])    
    print('sum of not drawn: ', loser.sumofnotdrawn())
    print('final number: ', number)
    print('answer: ', loser.sumofnotdrawn() * number)

    print("\ntotal time in s: {:5.5}".format(time.time() - start_time))
    