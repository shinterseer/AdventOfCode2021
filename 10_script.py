# import numpy as np
# import time
# import matplotlib.pyplot as plt

def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def get_clean_lines(filename):
    lines = get_lines(filename)
    clean = []
    for line in lines:
        clean.append(line[:-1])
    return clean


class SyntaxChecker:
    def __init__(self):
        self.brackets_open = ('(','[','{','<')
        self.brackets_close = (')',']','}','>')
    
        self.brackets = {'(':')','[':']','{':'}','<':'>'}
        self.missing_scores = {')':3,']':57,'}':1197,'>':25137}
        self.completing_scores = {'(':1,'[':2,'{': 3, '<':4}
        
        self.errors = []
        
    def check_line(self,line):
        score = 0
        open_brackets = []
        for char in line:
            if char in self.brackets_open:
                open_brackets.append(char)
            if char in self.brackets_close:
                if self.brackets[open_brackets[-1]] == char:
                    open_brackets.pop()
                else:
                    score += self.missing_scores[char]
                    self.errors.append(char)
                    break
        return score
    
    
    def complete_line(self,line):
        #get open brackets
        open_brackets = []
        for char in line:
                
            if char in self.brackets_open:
                open_brackets.append(char)
            if char in self.brackets_close:
                if self.brackets[open_brackets[-1]] == char:
                    open_brackets.pop()
                else:
                    print('syntax error! this should not happen, when competing lines')
                    break

        # calculate score for closing
        total_score = 0
        for char in reversed(open_brackets):
            total_score = 5*total_score + self.completing_scores[char]
            
        return total_score


if __name__ == '__main__':

    filename = '10a_input.txt'
    # filename = '10a_input_test.txt'
    lines = get_clean_lines(filename)

    sc = SyntaxChecker()

    incomplete = []
    total_score = 0
    for line in lines:
        score = 0
        score = sc.check_line(line)
        if score > 0:
            total_score += score
        else:
            incomplete.append(line)
            
    print('Answer1: ', total_score)
    
    scores = []    
    for line in incomplete:
        scores.append(sc.complete_line(line))

    scores.sort()    
    print('Answer2: ', scores[int(len(scores)/2)])
        
    



        