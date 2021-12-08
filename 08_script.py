# import numpy as np
# import time
# import matplotlib.pyplot as plt

def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def get_digits(filename):
    lines = get_lines(filename)    
    in_list = []
    out_list = []
    for line in lines:
        line = line[:-1]
        myinput = line.split(' | ')[0].split(' ')
        myoutput = line.split(' | ')[1].split(' ')
        in_list.append(myinput)
        out_list.append(myoutput)
    return in_list, out_list


def question1(out_list):
    count = 0
    for digits in out_list:
        for digit in digits:
            if len(digit) in [2,4,3,7]:
                count += 1
    return count

def line_to_sets(line):
    # sets = set({})
    sets = []
    for string in line:
        # sets.add(set(string))
        sets.append(set(string))
    return sets


def get_translator_nts(line):
    # make dictionary: {0:set0, 1:set1, ...}
    nts = {} # translation of numbers to sets
    for item in line:
        if len(item) == 2:
            nts[1] = item
            line = [x for x in line if not(x == item)]
        if len(item) == 3:
            nts[7] = item
            line = [x for x in line if not(x == item)]
        if len(item) == 4:
            nts[4] = item
            line = [x for x in line if not(x == item)]
        if len(item) == 7:
            nts[8] = item
            line = [x for x in line if not(x == item)]
    # find 3
    for item in line:
        if len(item) == 5 and nts[1].issubset(item):
            nts[3] = item
            line = [x for x in line if not(x == item)]      
    # find 5
    for item in line:
        if (len(item) == 5 
            and (nts[4] - item).issubset(nts[1])):
            nts[5] = item
            line = [x for x in line if not(x == item)]
    # find 2
    for item in line:
        if len(item) == 5:
            nts[2] = item
            line = [x for x in line if not(x == item)]
    # find 6
    for item in line:
        if len(item) == 6 and not(nts[1].issubset(item)):
            nts[6] = item
            line = [x for x in line if not(x == item)]
    # find 9
    for item in line:
        if len(item) == 6 and nts[4].issubset(item):
            nts[9] = item
            line = [x for x in line if not(x == item)]
    # only 0 remaining
    nts[0] = line[0]
    return nts


def translate_set(myset,stn):
    for key in stn:
        if myset == stn[key]:
            return key

def translate_list(list_of_sets,stn):
    translation = []
    for item in list_of_sets:
        translation.append(translate_set(item,stn))
    return translation


def get_output(list_of_sets,stn):
    t = translate_list(list_of_sets,stn)
    return 1000*t[0] + 100*t[1] + 10*t[2] + t[3]


if __name__ == '__main__':

    # start_time = time.time()

    filename = '08a_input.txt'
    in_list, out_list = get_digits(filename)
    print('Answer1: ', question1(out_list))

    result = 0
    for i in range(len(in_list)):
        in_sets = line_to_sets(in_list[i])
        out_sets = line_to_sets(out_list[i])
        translate_nts = get_translator_nts(in_sets)
        output = get_output(out_sets, translate_nts)
        result += output
    print('Answer2: ',result)

        
    # test_in_list = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    # test_out_list = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    # in_sets = line_to_sets(test_in_list)
    # out_sets = line_to_sets(test_out_list)
    # translate_nts = get_translator_nts(in_sets)
    # output = get_output(out_sets, translate_nts)
    # print('test output: ', output)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    