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
    grid = np.zeros([num_lines,len_lines],dtype=np.int)
    for i in range(num_lines):
        grid[i,:] = get_gridline(lines[i])
    return grid
    

def check_validity(point,shape):
    row = point[0]
    col = point[1]
    if row < 0 or col < 0 or row >= shape[0] or col >= shape[1]:
        return False
    else:
        return True

def get_relative_val(grid, point, delta):
    row = point[0]
    col = point[1]
    target = [row + delta[0], col + delta[1]]
    if check_validity(target,shape):
        return grid[target[0],target[1]], True
    else:
        return 0, False

def check_minimum(grid,point):
    row = point[0]
    col = point[1]
    value = grid[row,col]
    
    #check up to four neighbours
    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    for delta in deltas:
        relval, valid = get_relative_val(grid, point, delta)
        if valid and relval <= value:
            return False
        
    # still here? must be minimum
    return True


def add_point_to_basin_list(point,grid,delta,add_this):
    value, valid = get_relative_val(grid, point, delta)
    if valid and value != 9:
        add_this.add((point[0] + delta[0], point[1] + delta[1]))
        

def grow_basin(basin,grid):
    add_this = set({})
    for point in basin:
        deltas = [(-1,0), (1,0), (0,-1), (0,1)]
        for delta in deltas:
            add_point_to_basin_list(point, grid, delta, add_this)
    basin = basin.union(add_this)
    return basin

def max_out_basin(basin,grid):
    while True:
        size = len(basin)
        basin = grow_basin(basin,grid)
        if size == len(basin):
            break
    return basin


if __name__ == '__main__':

    filename = '09a_input.txt'
    # filename = '09a_input_test.txt'
    grid = get_grid(filename)
    shape = grid.shape
    count = 0
    count_minima = 0
    lowpoints = []
    
    for x,y in np.ndindex(shape):
        if check_minimum(grid, [x,y]):
            lowpoints.append((x,y))
            count_minima += 1
            count += grid[x,y] + 1    
    print('Answer 1:', count)
    
    basin_list = []
    for lowpoint in lowpoints:
        basin = {lowpoint}
        basin = max_out_basin(basin, grid)   
        basin_list.append(basin)
    size_list = [len(basin) for basin in basin_list]
    size_list.sort()
    print('Answer 2:', size_list[-1]*size_list[-2]*size_list[-3])
        