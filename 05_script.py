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


def get_path1(pair):
    path = []
    # if first component is equal
    if pair[0][0] == pair[1][0]:
        # which one is greater
        if pair[0][1] >= pair[1][1]:
            for i in range(pair[1][1],pair[0][1]+1):
                path.append([pair[0][0],i])
        if pair[0][1] < pair[1][1]:
            for i in range(pair[0][1],pair[1][1]+1):
                path.append([pair[0][0],i])

    # if secondcomponent is equal
    if pair[0][1] == pair[1][1]:
        # which one is greater
        if pair[0][0] >= pair[1][0]:
            for i in range(pair[1][0],pair[0][0]+1):
                path.append([i,pair[0][1]])
        if pair[0][0] < pair[1][0]:
            for i in range(pair[0][0],pair[1][0]+1):
                path.append([i,pair[0][1]])
        
    return path


def get_path2(pair):
    path = []
    # if first component is equal
    if pair[0][0] == pair[1][0]:
        return get_path1(pair)
    # if secondcomponent is equal
    if pair[0][1] == pair[1][1]:
        return get_path1(pair)

    # not returned yet -> diagonal
    # who is greater in first component
    if pair[0][0] < pair[1][0]:
        sign1 = -1
        lesser1 = pair[0][0]
        greater1 = pair[1][0]
    else:
        sign1 = 1
        lesser1 = pair[1][0]
        greater1 = pair[0][0]
    # who is greater in second component
    if pair[0][1] < pair[1][1]:
        sign2 = -1
        lesser2 = pair[0][1]
        greater2 = pair[1][1]
    else:
        sign2 = 1
        lesser2 = pair[1][1]
        greater2 = pair[0][1]

    path = []
    # for i in range(lesser1,greater1+1):
    for i in range(greater1 - lesser1 + 1):
        if sign1 == 1 and sign2 == 1:
            path.append([lesser1 + i,lesser2 + i])
        if sign1 == -1 and sign2 == 1:
            path.append([greater1 - i,lesser2 + i])
        if sign1 == 1 and sign2 == -1:
            path.append([lesser1 + i,greater2 - i])
        if sign1 == -1 and sign2 == -1:
            path.append([greater1 - i,greater2 - i])
        
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
        # print(pair)
        # input('press button')
        path1 = get_path1(pair)
        path2 = get_path2(pair)
        # print(path)
        # input('press button')
        for point in path1:
            field1[point[0],point[1]] += 1;
        for point in path2:
            field2[point[0],point[1]] += 1;
        # print_field(field,10)
        # input('press button')


    count1 = 0
    for x,y in np.ndindex(size,size):
        count1 += (field1[x,y] > 1)

    count2 = 0
    for x,y in np.ndindex(size,size):
        count2 += (field2[x,y] > 1)

        
    print('Part1 answer: ', count1)
    print('Part2 answer: ', count2)
    print("\ntotal time in s: {:5.5}".format(time.time() - start_time))
    