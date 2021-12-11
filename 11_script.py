import numpy as np
# import time
# import matplotlib.pyplot as plt


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines


def get_field(filename):
    lines = get_lines(filename)
    size = 10
    array = np.zeros((size,size),dtype = np.int8)
    for i in range(len(lines)):
        string = lines[i][:-1]
        array[i,:] = np.array(list(string))
    return array


def check_validity(point,shape):
    row = point[0]
    col = point[1]
    if row < 0 or col < 0 or row >= shape[0] or col >= shape[1]:
        return False
    else:
        return True


class OctoCave:
    def __init__(self,array):
        self.field = array.copy()
        self.has_flashed = np.zeros(array.shape)
        self.num_flashes = 0
        
    def check_sync_flash(self):
        for (row,col) in np.ndindex(self.field.shape):
            if not(self.has_flashed[row,col]):
                return False
        return True

    def new_timestep(self):
        for (row,col) in np.ndindex(self.field.shape):
            if self.field[row,col] > 9:
                self.field[row,col] = 0
            self.has_flashed[row,col] = 0


    def pass_time(self):
        shape = self.field.shape
        for row,col in np.ndindex(shape):
            self.age((row,col))

    def age(self,point):
        row = point[0]
        col = point[1]
        self.field[row,col] += 1
        if self.field[row,col] > 9:            
            self.flash(point)

    def flash(self,point):
        row = point[0]
        col = point[1]
        if (self.has_flashed[row,col]):
            return None
        self.has_flashed[row,col] = 1
        self.num_flashes += 1
        deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for delta in deltas:
            target = (row + delta[0], col + delta[1])
            if check_validity(target,self.field.shape):
                self.age(target)


if __name__ == '__main__':

    filename = '11a_input.txt'
    # filename = '11a_input_test.txt'
    field = get_field(filename)
    oc = OctoCave(field)
    sync_flash = []
    for i in range(100):
        oc.pass_time()
        oc.new_timestep()
    print('Answer 1: ',oc.num_flashes)

    oc = OctoCave(field)
    step = 0
    while True:
        oc.pass_time()
        step += 1
        if oc.check_sync_flash():
            break
        oc.new_timestep()
    print('Answer 2: ',step)

    
    
    
