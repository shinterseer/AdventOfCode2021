# import numpy as np
import time


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def get_caves(filename):
    lines = get_lines(filename)
    caves = [cave[:-1].split('-') for cave in lines]
    return caves


class Cave:
    def __init__(self,name):
        self.name = name
        self.connections = set([])
        if name.isupper():            
            self.is_big = True
        else:
            self.is_big = False


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        

    def setup(self,list_of_edges):
        self.edges = list_of_edges
        nodeset = set({})
        for edge in list_of_edges:
            nodeset.add(edge[0])
            nodeset.add(edge[1])
        for node in nodeset:
            self.nodes[node] = Cave(node)

    def setup_connections(self):
        for edge in self.edges:
            self.nodes[edge[0]].connections.add(edge[1])
            self.nodes[edge[1]].connections.add(edge[0])



def get_legal_steps1(graph,path):
    con = path[-1].connections
    legal = []
    # there are no legal moves from 'end'
    if path[-1].name == 'end':
        return []
    for c in con:
        other = graph.nodes[c]
        if other.is_big:
            legal.append(other)
        else:
            if not(other in path):
                legal.append(other)
    return legal # list of nodes that are legal next steps


def get_legal_steps2(graph,path):
    con = path[-1].connections
    legal = []
    took_2nd_small = False
    
    # check if we already used our "visit small cave twice" - thing
    for i in range(len(path)):
        node = path[i]
        if not(node.is_big):
            for node2 in path[i+1:]:
                if node2 == node:
                    took_2nd_small = True
    
    # there are no legal moves from 'end'
    if path[-1].name == 'end':
        return []
        
    for c in con:
        other = graph.nodes[c]
        if other.is_big:
            legal.append(other)
        elif not(other.name == 'start') and not(took_2nd_small):
            legal.append(other)
        else:
            if not(other in path):
                legal.append(other)
    return legal # list of nodes that are legal next steps

    

def complete_path(graph,path,part1=True):
    cnode = path[-1]
    open_poss = [] # open possibilities
    while True:
        # get legal steps
        if part1:
            legal = get_legal_steps1(graph, path)
        else:
            legal = get_legal_steps2(graph, path)
        
        # if no legal steps: break
        if len(legal) == 0:
            break
        
        # go one step
        path.append(legal[0])
        cnode = legal[0]
        legal.pop(0)
        open_poss.append(legal.copy())
        if cnode.name == 'end':
            break
        
    return path, open_poss
    

def get_latest_open_poss(path,poss):
    # index = None
    for i in range(len(path)-1,0,-1):
        if len(poss[i-1]) >= 1:
            # index = i-1
            return i-1
    # return index


def find_all_paths(caves,part1=True):
    
    relevant_paths = []
    all_paths = []
    # go one random path
    start = caves.nodes['start']
    if part1:
        path, open_poss = complete_path(caves, [start])
    else:
        path, open_poss = complete_path(caves, [start], part1=False)
        
    # when at end: if final step == 'end' apend to list
    all_paths.append(path)
    if path[-1].name == 'end':
        relevant_paths.append(path)

    while True:
        # go back until you have a point with open possibilities.
        #--------------------------------------------------------        
        index = get_latest_open_poss(path, open_poss)
        # if no open possibilies: break
        if index == None:
            break
        # trim path and possibilities list
        path = path[:index+1] # partial path to latest open possibility
        open_poss = open_poss[:index+1] # partial path to latest open possibility

        # take one step in that direction and complete the path
        # ------------------------------------------------------
        path.append(open_poss[index][0]) # step in that direction
        open_poss[index].pop(0) # remove the chosen possibility
        if part1:
            path, more_poss = complete_path(caves, path) # complete the path
        else:
            path, more_poss = complete_path(caves, path, part1=False) # complete the path  
        #update possibility list
        open_poss = open_poss + more_poss
        
        # append path to corresponding list (all or relevant)
        # ----------------------------------------------------
        all_paths.append(path)
        if path[-1].name == 'end':
            relevant_paths.append(path)
    return all_paths, relevant_paths

        
def print_nodes(nodelist):
    for node in nodelist:
        print(node.name)


if __name__ == '__main__':
    timer = time.time()
    
    # Get Data
    filename = '12a_input.txt'
    # filename = '12a_input_test.txt'
    lines = get_lines(filename)
    cave_data = get_caves(filename)
    
    cave_system = Graph()
    cave_system.setup(cave_data)
    cave_system.setup_connections()
    
    # Part 1
    all_paths, relevant_paths = find_all_paths(cave_system)    
    print('Answer 1: ',len(relevant_paths))

    # Part 2
    all_paths, relevant_paths = find_all_paths(cave_system,part1=False)
    print('Answer 2: ', len(relevant_paths))

    print('execution time in s: {:3.3}'.format(time.time() - timer))
    
    
