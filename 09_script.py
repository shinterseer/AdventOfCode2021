import numpy as np
# import time
# import matplotlib.pyplot as plt

def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines


def get_gridline(line):
    npline = np.array([int(string) for string in list(line) 
                       if not(string == '\n')])
    return npline
    
def get_grid(filename):
    lines = get_lines(filename)
    num_lines = len(lines)
    len_lines = len(get_gridline(lines[0]))
    grid = np.zeros([num_lines,len_lines],dtype=int)
    for i in range(num_lines):
        grid[i,:] = get_gridline(lines[i])
    return grid
    

def check_minimum(grid,point):
    row = point[0]
    col = point[1]
    value = grid[row,col]
    #check top
    try:
        if grid[row-1,col] <= value:
            return False
    except:
        pass
    #check bottom
    try:
        if grid[row+1,col] <= value:
            return False
    except:
        pass
    #check left
    try:
        if grid[row,col-1] <= value:
            return False
    except:
        pass
    #check right
    try:
        if grid[row,col+1] <= value:
            return False
    except:
        pass
    
    # still here? must be minimum
    return True

if __name__ == '__main__':

    filename = '09a_input.txt'
    # filename = '09a_input_test.txt'
    grid = get_grid(filename)
    shape = grid.shape
    count = 0
    count_minima = 0
    minima = []
    
    for x,y in np.ndindex(shape):
        if check_minimum(grid, [x,y]):
            minima.append(grid[x,y])
            count_minima += 1
            count += grid[x,y] + 1
            # print('minimmum nr. : ', count_minima)
            # print('found minimum at: ',x,y)
            # print('value: ',grid[x,y])
            # print('neighbour top: ',grid[max(x-1,0),y])
            # print('neighbour bot: ',grid[min(x+1,shape[0]-1),y])
            # print('neighbour left: ',grid[x,max(y-1,0)])
            # print('neighbour right: ',grid[x,min(y+1,shape[1]-1)])
            # input('press button')
    
    print('Answer 1:', count)    
    print('Answer 1:', count_minima)    
    
    
    
    
    
    
    
    
    
    
    