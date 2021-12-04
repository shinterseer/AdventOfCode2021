def get_strings(filename):
    file = open(filename)
    lines = file.readlines()
    strings = []
    for line in lines:
        strings.append(line[:-1])
    
    file.close()
    return strings


def most_common_bit(strings,pos):
    count0 = 0
    for string in strings:
        count0 += (string[pos] == '0')
    if count0 > len(strings)/2:
        return '0'
    else: 
        return '1'


def least_common_bit(strings,pos):
    if most_common_bit(strings, pos) == '1':
        return '0'
    else:
        return '1'

def get_epsilon(strings):
    epsilon = ''
    length = len(strings[0])
    for i in range(length):
        epsilon += least_common_bit(strings,i)
    return epsilon


def get_gamma(strings):
    gamma = ''
    length = len(strings[0])
    for i in range(length):
        gamma += most_common_bit(strings,i)
    return gamma


def reduce_strings(strings,pos,mode):
    reduced = []
    most_common = most_common_bit(strings, pos)
    for string in strings:
        if mode == 'oxygen':
            if string[pos] == most_common:
                reduced.append(string)
        if mode == 'CO2':
            if not(string[pos] == most_common):
                reduced.append(string)
            
    return reduced


def my_fun(a,b,c):
    print('my_fun was called')

if __name__ == '__main__':
    filename = '03a_input.txt'
    strings = get_strings(filename)
    
    print('Part1')
    gamma = get_gamma(strings)
    epsilon = get_epsilon(strings)
    print("gamma = ", gamma, "in decimal: ", int(gamma,2))
    print("epsilon = ", epsilon, "in decimal: ", int(epsilon,2))
    print("gamma * epsilon: ", int(gamma,2)*int(epsilon,2))
    
    print('\nPart2')
    length = len(strings[0])
    reduced = strings
    for pos in range(length):
        reduced = reduce_strings(reduced, pos, 'oxygen')
        if len(reduced) == 1:
            oxygen = int(reduced[0],2)
            break
    print('oxygen rating: ',oxygen)
    
    reduced = strings
    for pos in range(length):
        reduced = reduce_strings(reduced, pos, 'CO2')
        if len(reduced) == 1:
            CO2 = int(reduced[0],2)
            break
    print('CO2 rating: ',CO2)
    print('oxygen* CO2: ', oxygen*CO2)
    