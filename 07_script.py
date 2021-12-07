import numpy as np
import time
import matplotlib.pyplot as plt

def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def sum_to_n(n):
    return n*(n+1) / 2

def fuel_cost1(positions, point):
    cost = 0
    for pos in positions:
        cost += abs(pos - point)
    return cost


def fuel_cost2(positions, point):
    cost = 0
    for pos in positions:
        dist = abs(point - pos)
        cost += sum_to_n(dist)
    return cost


def convergence_step(positions,mmin,mmax):
    mid = .5*(mmax + mmin)
    up = fuel_cost2(positions,mid + 1)
    down = fuel_cost2(positions,mid - 1)
    if up > down:
        return mmin, mid
    else:
        return mid, mmax


def convergence_scheme(positions,mmin,mmax):
    steps = 0
    while True:
        mmin_old = mmin
        mmax_old = mmax
        mmin, mmax = convergence_step(positions,mmin,mmax)
        steps += 1
        if (abs(mmin - mmin_old) < 1) and (abs(mmax - mmax_old) < 1): break
        if steps > 1000: break
    return mmin, mmax, steps


if __name__ == '__main__':

    start_time = time.time()

    filename = '07a_input.txt'
    lines = get_lines(filename)
    positions = lines[0].split(',')
    # test_postitions = [16,1,2,0,4,2,7,1,2,14]
    positions = np.array([int(pos) for pos in positions])
    optimal1 = round(np.median(positions))
    print("Answer 1: ", fuel_cost1(positions,optimal1))
    
    #I dunno, why we have to subtract 1 here. result is somting.55
    # so rounding up should be a little better
    # oh well... 
    optimal2 = round(np.average(positions))-1
    print("Answer 2: ", fuel_cost2(positions,optimal2))
    
    
    # but if you like numerics... you write an iteration scheme...
    bottom, top, steps = convergence_scheme(positions, -1000, 2000)
    optimal2 = round((bottom+top)*.5)
    print("Answer 2 (cool version): ", fuel_cost2(positions,optimal2))
    print("concergence after ", steps, "steps")
    