import numpy as np
import time


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines


def get_data(filename):
    lines = get_lines(filename)
    initial = list(lines[0][:-1])
    rules = []
    for line in lines[2:]:
        temp = line[:-1].split(' -> ')
        rules.append([list(temp[0]),temp[1]])
    return initial, rules


def get_min_max(count):
    mymin = count['B']
    mymax = count['B']
    minkey = 'B'
    maxkey = 'B'
    for key in count:
        if count[key] < mymin:
            mymin = count[key]
            minkey = key
        if count[key] > mymax:
            mymax = count[key]
            maxkey = key
    return minkey, maxkey


class Polymer():
    def __init__(self,state,rules):
        self.rules = rules
        self.state = state
        # self.pair_count = count_pairs(state,rules)
        self.chars = self.get_chars()
        self.elem_count = self.count_elements()
        self.pair_count = self.count_pairs()


    @staticmethod
    def get_chars():
        return ['B','C','F','H','K','N','O','P',
                'S','V']


    def count_pairs(self):
        count_pairs = {}
        for char1 in self.chars:
            for char2 in self.chars:
                counter = 0
                for i in range(len(self.state)-1):
                    if self.state[i]+self.state[i+1] == char1+char2:
                        counter +=1
                count_pairs[char1+char2] = counter    
        return count_pairs


    def count_elements(self):
        # chars = get_chars()
        count = {}
        for char in self.chars:
            counter = 0
            for element in self.state:
                if element == char:
                    counter += 1
            count[char] = counter
        return count


    def step(self):

        elem_summand = {}
        pair_summand = {}

        # initialize summands
        for char1 in self.chars:
            elem_summand[char1] = 0
            for char2 in self.chars:                
                pair_summand[char1+char2] = 0
        
        for rule in self.rules:
            rule_string = rule[0][0] + rule[0][1]
            rule_insert = rule[1]
            # contribute to element summand dict
            elem_summand[rule_insert] += self.pair_count[rule_string]
            
            # contribute to pair summand dict
            # pair was destroyed by insertion
            pair_summand[rule_string] -= self.pair_count[rule_string]
            # two new pairs were chreated
            pair1 = rule_string[0] + rule_insert
            pair2 = rule_insert + rule_string[1]            
            pair_summand[pair1] += self.pair_count[rule_string]
            pair_summand[pair2] += self.pair_count[rule_string]
        
        # update dictionaries
        for key in self.elem_count:
            self.elem_count[key] += elem_summand[key]
        for key in self.pair_count:
            self.pair_count[key] += pair_summand[key]


if __name__ == '__main__':
    timer = time.time()
        
    # Get Data
    filename = '14a_input.txt'
    # filename = '14a_input_test.txt'
    lines = get_lines(filename)
    initial, rules = get_data(filename)

    # Part 1    
    pol1 = Polymer(initial.copy(),rules)
    for i in range(10):
        pol1.step()    
    minkey,maxkey = get_min_max(pol1.elem_count)
    print('Answer 1: ',pol1.elem_count[maxkey] - pol1.elem_count[minkey])

    # Part 2
    pol2 = Polymer(initial.copy(),rules)
    for i in range(40):
        pol2.step()    
    minkey,maxkey = get_min_max(pol2.elem_count)
    print('Answer 2: ',pol2.elem_count[maxkey] - pol2.elem_count[minkey])
    
    print('execution time in s: {:3.3}'.format(time.time() - timer))
    
