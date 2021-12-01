

def count_increases(numbers):
    counter = 0
    for i in range(1,len(numbers)):
        if (numbers[i] > numbers[i-1]):
            counter += 1
    return counter


def get_three_sums(numbers):
    three_sums = []
    for i in range(len(numbers)-2):
        three_sums.append(numbers[i] + numbers[i+1] + numbers[i+2])
    return three_sums


def get_numbers(filename):
    file = open(filename)
    lines = file.readlines()
    #numbers = [int(lines[i]) for i in range(len(lines))]
    numbers = [int(line) for line in lines]
    file.close()
    return numbers


if __name__ == "__main__":
    
    numbers = get_numbers("01a_input.txt")
    
    answer1 = count_increases(numbers)
    three_sums = get_three_sums(numbers)
    answer2 = count_increases(three_sums)

    print("answer1: ", answer1)    
    print("answer2: ", answer2)