import numpy as np
import time


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

class FishPop:
    def __init__(self,pagelist):
        self.agelist = pagelist

    def age(self):
        next_age = np.zeros(9)
        for i in range(8):
            next_age[i] = self.agelist[i+1]
        next_age[6] += self.agelist[0]
        next_age[8] = self.agelist[0]
        
        self.agelist = next_age


if __name__ == '__main__':

    start_time = time.time()

    filename = '06a_input.txt'
    lines = get_lines(filename)
    fishtimers = [int(str) for str in lines[0].split(',')]
    
    fish_pop_start = np.zeros(9, dtype = np.ulonglong)
    for i in range(9):
        fish_pop_start[i] = len([fish for fish in fishtimers if fish == i])

    fishpop1 = FishPop(fish_pop_start)
    fishpop2 = FishPop(fish_pop_start)
    
    for i in range(80):
        fishpop1.age()
    ans1 = int(fishpop1.agelist.sum())

    for i in range(256):
        fishpop2.age()
    ans2 = int(fishpop2.agelist.sum())
        
    print('Part1 answer: ', ans1)        
    print('Part2 answer: ', ans2)
    print("\ntotal time in s: {:5.5}".format(time.time() - start_time))
    

