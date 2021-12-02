import numpy as np


class UBoat:
    pos = np.array([0,0])
    aim = np.array([0,0])

    def UBoat(self):
        self.pos = np.array([0,0])
        self.aim = np.array([0,0])

    def move_p1(self,command):
        if command[0] == 'forward':
            self.pos += np.array([command[1], 0])
        if command[0] == 'up':
            self.pos += np.array([0, (-1)*command[1]])
        if command[0] == 'down':
            self.pos += np.array([0, command[1]])

    def move_p2(self,command):
        if command[0] == 'forward':
            self.pos = self.pos + np.array([command[1], 0])
            self.pos = self.pos + command[1] * self.aim
        if command[0] == 'up':
            self.aim += ([0, (-1)*command[1]])
        if command[0] == 'down':
            self.aim += ([0, command[1]])
            

def get_commands(filename):
    file = open(filename)
    lines = file.readlines()
    commands = []
    for line in lines:
        command = line[:line.find(" ")]
        amount = int(line[line.find(" "):])
        commands.append([command, amount])
    
    file.close()
    return commands



if __name__ == "__main__":
    
    commands = get_commands("02a_input.txt")
    
    print('Part1')
    myboat = UBoat()
    for command in commands:
        myboat.move_p1(command)
    print('final postion: ',myboat.pos)
    print("answer part 1: ", myboat.pos[0]*myboat.pos[1])

    print('\nPart2')
    myboat = UBoat()
    myboat.pos = np.array([0,0])
    for command in commands:
        myboat.move_p2(command)
    print('final postion: ',myboat.pos)
    print("answer part 2: ", myboat.pos[0]*myboat.pos[1])

