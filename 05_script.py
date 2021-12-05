import numpy as np
import time


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines


def get_numbers(filename):
    lines = get_lines(filename)
    numbers = []
    for line in lines:
        strings1 = line.split('->')[0].split(',')
        strings2 = line.split('->')[1].split(',')
        numbers1 = [int(string) for string in strings1]
        numbers2 = [int(string) for string in strings2]
        numbers.append([numbers1, numbers2])
    return numbers


def get_path(pair, part1=True):
    start = np.array(pair[0])
    end = np.array(pair[1])
    direction = np.sign(end-start)
    if part1:
        # check if diagonal        
        if direction.dot(direction) > 1:
            return []
    path = [start]
    current = start
    while True:
        current = current + direction
        path.append(current)
        if (current == end).all():
            break
    return path

def print_field(field,size):
    for i in range(size):
        print(field[i,:])

if __name__ == '__main__':

    start_time = time.time()
    filename = '05a_input.txt'
    # filename = '05a_input_test.txt'
    lines = get_lines(filename)
    numbers = get_numbers(filename)
    size = 1000
    field1 = np.zeros([size,size])
    field2 = np.zeros([size,size])
    for pair in numbers:
        path1 = get_path(pair, part1=True)
        path2 = get_path(pair, part1=False)
        for point in path1:
            field1[point[0],point[1]] += 1;
        for point in path2:
            field2[point[0],point[1]] += 1;

    count1 = 0
    for x,y in np.ndindex(size,size):
        count1 += (field1[x,y] > 1)

    count2 = 0
    for x,y in np.ndindex(size,size):
        count2 += (field2[x,y] > 1)

        
    print('Part1 answer: ', count1)
    print('Part2 answer: ', count2)
    print("\ntotal time in s: {:5.5}".format(time.time() - start_time))
    

