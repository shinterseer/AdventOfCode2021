import numpy as np
import time


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def get_input(filename):
    lines = get_lines(filename)
    points = []
    for line in lines:
        if line == '\n':
            break
        pair = line[:-1].split(',')
        points.append([int(pair[0]), int(pair[1])])
        
    folds = []
    for i in range(len(points)+1,len(lines)):
        pair = lines[i].split('=')
        folds.append([pair[0],int(pair[1])])
    return points, folds


def fold(points,fold):
    rowfold = False
    if fold[0] == 'fold along y':
        rowfold = True
    
    fv = fold[1] # fold value
    if rowfold:
        fi = 1 # fold index ... x(col):1, y(row):0
    else:
        fi = 0
        
    for point in points:
        if point[fi] > fv:
            point[fi] += -2*(point[fi] - fv)
    
    points = make_unique(points)
    return points


def make_unique(mylist):
    '''
    returns list with unique items. might screw up sequence
    '''
    unique = []
    for item in mylist:
        if not(item in unique):
            unique.append(item)
    return unique


def print_page(points,size=100):
    field = np.zeros((size,size))
    for point in points:
        field[point[0],point[1]] = 1        
        
    for i in range(size):
        for j in range(size):
            if field[j,i] == 1:
                print('#',end='')
            else:
                print('.',end='')            
        print('')


if __name__ == '__main__':
    timer = time.time()
        
    # Get Data
    filename = '13a_input.txt'
    # filename = '13a_input_test.txt'
    points,folds = get_input(filename)

    # Part 1
    points = fold(points,folds[0])
    print('Answer 1: ',len(points))

    # Part 2
    for i in range(1,len(folds)):
        points = points = fold(points,folds[i])
    print('Answer 2:')
    print('')
    print_page(points,size=50)
    print('')
    print('execution time in s: {:3.3}'.format(time.time() - timer))
    
